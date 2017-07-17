import numpy as np
import bisect

import pybasis
import pyam
import read_matel

np.set_printoptions(threshold=np.nan)

nParticles = 2  # number of particles in simulation

def set_up_sp_basis(filename):
    with open(filename) as fp:
        orbitals = pybasis.nlj_orbital.ParseOrbitalPNStream(fp, True)

    sp_subspace = pybasis.m_scheme.SingleParticleSubspacePN(
        pybasis.nlj_orbital.OrbitalSpeciesPN.kN, orbitals
        )

    return sp_subspace

# this is a recursive function, so the function call is a bit funny
def makeSDs(sp_states, num_particles, mb_states=[], current_state=[]):
    # if the state is full, add it
    if len(current_state) == num_particles:
        # necessary if-test variables
        pairStatement = True

        # SD state space restrictions
        restrictSpin = True
        restrictPairs = False

        # check spin conservation (M=0)
        if restrictSpin:
            spin = sum([float(sp_states[i].m()) for i in current_state])
        else:
            spin = 0
        # restrict to pair model
        if restrictPairs:
            for i in range(0, len(current_state), 2):
                if not ((current_state[i] % 2 == 0) and (current_state[i]+1 == current_state[i+1])):
                    pairStatement = False

        if (spin == 0) and pairStatement:
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
            makeSDs(sp_states, num_particles, mb_states, new_state)
    return mb_states

def makeOneBodyInts(sp_states):
    oneBodyInts = {}
    for p in range(0, len(sp_states)):
        matel = states[p].n()
        oneBodyInts[(p, p)] = matel
    return oneBodyInts

def makeTwoBodyInts(sp_states):
    twoBodyInts = {}
    for p in range(0, len(sp_states)):
        for q in range(p+1, len(sp_states)):
            for r in range(0, len(sp_states)):
                for s in range(r+1, len(sp_states)):
                    # pairing model
                    if (p+1 == q) and (r+1 == s) and (p % 2 == 0) and (r % 2 == 0):
                        twoBodyInts[((p, q), (r, s))] = -g
    return twoBodyInts

def OneBodyHamiltonian(mb_basis, one_body_matels):
    hamiltonian_matrix = np.zeros((len(mb_basis), len(mb_basis)))
    for i in range(0, len(mb_basis)):
        ket = mb_basis[i]
        for labels, matel in one_body_matels.items():
            if len(np.intersect1d(labels, ket)) == 1:
                hamiltonian_matrix[i, i] += matel
    return hamiltonian_matrix

def apply_two_body_operator(labels, ket):
    create_ops, annihilate_ops = labels

    phase = 0
    try:
        for op in reversed(annihilate_ops):
            idx = ket.index(op)
            phase += idx
            ket.pop(idx)
        for op in create_ops:
            idx = bisect.bisect_left(ket, op)
            if (idx < len(ket)) and (ket[idx] == op):
                raise ValueError
            phase += idx
            ket.insert(idx, op)
    except ValueError:
        return (None, 0)

    return (ket, (-1)**(phase % 2))

def TwoBodyHamiltonian(mb_basis, two_body_matels):
    hamiltonian_matrix = np.zeros((len(mb_basis), len(mb_basis)))
    num_particles = len(mb_basis[0])
    ct = 0
    for i in range(0, len(mb_basis)):
        for labels, matel in two_body_matels.items():
            ket = mb_basis[i][:]
            bra, phase = apply_two_body_operator(labels, ket[:])
            if bra is None:
                bra, phase = apply_two_body_operator(reversed(labels), ket[:])
            if bra is None:
                continue
            # if (labels[0] == labels[1]):
            #     phase *=2
            for j in range(0, len(mb_basis)):
                test_bra = mb_basis[j]
                if bra == test_bra:
                    hamiltonian_matrix[j, i] += matel*phase
                    # hamiltonian_matrix[i, j] += matel*phase/4

    return hamiltonian_matrix


sp_states = set_up_sp_basis('sd_orbitals.dat')
print("Single particle states:")
print(sp_states.DebugStr(), "\n\n")

SD_states = makeSDs(sp_states, nParticles)

ob_matel, tb_matel = read_matel.read_m_scheme_matel('sdshellint.dat', sp_states)

H = OneBodyHamiltonian(SD_states, ob_matel) + TwoBodyHamiltonian(SD_states, tb_matel)

np.savetxt('Hamiltonian.txt', H, '%5.2f')
# import matplotlib.pyplot as plt
# plt.imshow(H)
# plt.show()

w, v = np.linalg.eigh(H)

print("")
#print(np.sort(np.real(w)))
print(np.sort(w))
