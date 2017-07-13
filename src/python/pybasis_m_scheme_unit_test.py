import pybasis
import pyam

fp = open('orbitals.dat')
orbitals = pybasis.nlj_orbital.ParseOrbitalPNStream(fp, True)

sp_space = pybasis.m_scheme.SingleParticleSpacePN(orbitals)
print(sp_space.DebugStr())

subspace = pybasis.m_scheme.SingleParticleSubspacePN(pybasis.nlj_orbital.OrbitalSpeciesPN.kP,orbitals)
print(subspace.DebugStr())
state = pybasis.m_scheme.SingleParticleStatePN(subspace, 0)
print(state.labels())

print(subspace.GetStateLabels(0))
