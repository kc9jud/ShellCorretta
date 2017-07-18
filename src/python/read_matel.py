import numpy as np
import pybasis
import pyam

def skip_comments(fp):
    while True:
        line = next(fp)
        # ignore comment lines
        if line[0] != '#':
            return line

def scale_factor(A):
    return (18/A)**(.3)

def read_m_scheme_matel(filename, sp_basis, scale_factor=1.0):
    ob_matel = {}
    tb_matel = {}

    index_mapping = {}
    num_sp_energies = -1
    with open(filename) as fp:
        line = skip_comments(fp)
        num_sp_energies = int(line)
        if num_sp_energies != len(sp_basis):
            raise ValueError("Invalid number of s.p. energies")

        for _ in range(num_sp_energies):
            line = skip_comments(fp)
            tokens = line.split()
            idx = int(tokens[0])
            n = int(tokens[1])
            l = int(tokens[2])
            j = pyam.HalfInt(int(tokens[3]), 2)
            m = pyam.HalfInt(int(tokens[4]), 2)
            en = float(tokens[5])
            sp_index = sp_basis.LookUpStateIndex((n, l, j, m))

            index_mapping[idx] = sp_index
            ob_matel[(sp_index, sp_index)] = en

        line = skip_comments(fp)
        num_tb_matels = int(line)
        for _ in range(num_tb_matels):
            line = skip_comments(fp)
            tokens = line.split()
            idx_p = index_mapping[int(tokens[0])]
            idx_q = index_mapping[int(tokens[1])]
            idx_r = index_mapping[int(tokens[2])]
            idx_s = index_mapping[int(tokens[3])]
            matel = float(tokens[4])

            tb_matel[((idx_p, idx_q), (idx_r, idx_s))] = matel*scale_factor

    return (ob_matel, tb_matel)


if __name__ == "__main__":
    def set_up_sp_basis(filename):
        with open(filename) as fp:
            orbitals = pybasis.nlj_orbital.ParseOrbitalPNStream(fp, True)

        sp_subspace = pybasis.m_scheme.SingleParticleSubspacePN(
            pybasis.nlj_orbital.OrbitalSpeciesPN.kN, orbitals
            )

        return sp_subspace

    sp_basis = set_up_sp_basis('sd_orbitals.dat')
    ob_matel, tb_matel = read_m_scheme_matel('sdshellint.dat', sp_basis)
    print(sorted(ob_matel.items()))
    print(sorted(tb_matel.items()))
