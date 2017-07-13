import pybasis
import pyam

fp = open('orbitals.dat')
orbitals = pybasis.nlj_orbital.ParseOrbitalPNStream(fp, True)

for orb in orbitals:
    print(orb)

for orb in orbitals:
    print(orb.Key())
