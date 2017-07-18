import numpy as np
import bisect

import pybasis
import pyam
import read_matel

np.set_printoptions(threshold=np.nan)


def set_up_sp_basis(filename):
    with open(filename) as fp:
        orbitals = pybasis.nlj_orbital.ParseOrbitalPNStream(fp, True)

    sp_subspace = pybasis.m_scheme.SingleParticleSubspacePN(
        pybasis.nlj_orbital.OrbitalSpeciesPN.kN, orbitals
        )

    return sp_subspace


# this is a recursive function, so the function call is a bit funny
def makeSDs(sp_states, num_particles, m=None, only_pairs=False, mb_states=[], current_state=[]):
    # if the state is full, add it
    if len(current_state) == num_particles:
        # necessary if-test variables
        pairStatement = True

        # check total m value
        if m is not None:
            two_spin = sum([sp_states[i].m().TwiceValue() for i in current_state])
            if two_spin/2. != m:
                return mb_states

        # restrict to pair model
        if only_pairs:
            for i in range(0, len(current_state), 2):
                if not ((current_state[i] % 2 == 0) and (current_state[i]+1 == current_state[i+1])):
                    return mb_states

        # append Slater determinant to list of Slater determinants
        mb_states.append(current_state[:])

    # still need more particles
    else:
        # if list is empty, "previous index" is -1
        try:
            prevIndex = current_state[-1]
        except IndexError:
            prevIndex = -1
        for i in range(prevIndex+1, len(sp_states)):
            new_state = current_state + [i]
            makeSDs(sp_states, num_particles, m, only_pairs, mb_states, new_state)
    return mb_states


def ob_hamiltonian(mb_basis, one_body_matels):
    hamiltonian_matrix = np.zeros((len(mb_basis), len(mb_basis)))
    for i in range(0, len(mb_basis)):
        ket = mb_basis[i]
        for labels, matel in one_body_matels.items():
            if len(np.intersect1d(labels, ket)) == 1:
                hamiltonian_matrix[i, i] += matel
    return hamiltonian_matrix


def apply_operator(labels, ket):
    create_ops, annihilate_ops = labels

    g = 0
    try:
        for op in annihilate_ops:
            idx = ket.index(op)
            g += idx
            ket.pop(idx)
        for op in reversed(create_ops):
            idx = bisect.bisect_left(ket, op)
            if (idx < len(ket)) and (ket[idx] == op):
                raise ValueError
            g += idx
            ket.insert(idx, op)
    except ValueError:
        return (None, 0)

    return (ket, (-1)**(g % 2))


def tb_hamiltonian(mb_basis, two_body_matels):
    hamiltonian_matrix = np.zeros((len(mb_basis), len(mb_basis)))
    for i in range(0, len(mb_basis)):
        ket = mb_basis[i]
        for labels, matel in two_body_matels.items():
            bra, phase = apply_operator(labels, ket[:])
            if bra is None:
                    continue
            if bra == ket:
                hamiltonian_matrix[i, i] += matel*phase
            else:
                for j in range(0, i):
                    test_bra = mb_basis[j]
                    if bra == test_bra:
                        hamiltonian_matrix[j, i] += matel*phase
                        hamiltonian_matrix[i, j] += matel*phase

    return hamiltonian_matrix


if __name__ == "__main__":
    import argparse

    parser =  argparse.ArgumentParser(description="sd-shell model code")
    parser.add_argument("--orbital-file", help="orbital file", type=str, default="sd_orbitals.dat")
    parser.add_argument("--interaction-file", help="interaction file", type=str, default="sdshellint.dat")
    parser.add_argument("N", help="number of valence neutrons", type=int)
    parser.add_argument("M", help="total M", type=float)
    args = parser.parse_args()

    sp_states = set_up_sp_basis(args.orbital_file)
    print("Single particle states:")
    print(sp_states.DebugStr(), "\n\n")

    SD_states = makeSDs(sp_states, args.N, args.M)

    scale_factor = read_matel.scale_factor(16+args.N)
    ob_matel, tb_matel = read_matel.read_m_scheme_matel(args.interaction_file, sp_states, scale_factor)

    H = ob_hamiltonian(SD_states, ob_matel) + tb_hamiltonian(SD_states, tb_matel)

    w, v = np.linalg.eigh(H)

    print("")
    #print(np.sort(np.real(w)))
    print(np.sort(w))
