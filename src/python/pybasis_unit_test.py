import pybasis
import pyam

fp = open('orbitals.dat')
orbitals = pybasis.ParseOrbitalPNStream(fp, True)

for orb in orbitals:
    print(orb)

for orb in orbitals:
    print(orb.Key())
