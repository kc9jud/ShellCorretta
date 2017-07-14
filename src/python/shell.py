import numpy as np

import pybasis
import pyam

np.set_printoptions(threshold=np.nan)

nParticles = 4         #number of particles in simulation
nLevels    = 4         #number of shells we include in our calculation
nStates    = 2*nLevels #number of states available for a given number of levels

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
            mb_states.append(np.asarray(current_state))

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


states = set_up_sp_basis('orbitals.dat')
print("Single particle states:")
print(states.DebugStr(),"\n\n")

SD_states = makeSDs(states, nParticles)
print(np.asarray(SD_states))

def makeOneBodyInts(sp_states):
    oneBodyInts = []
    for p in range(0, len(sp_states)):
        matel = states[p].n()
        oneBodyInts.append(np.asarray([p, p, matel]))
    return oneBodyInts

def makeTwoBodyInts(sp_states):
    twoBodyInts = []
    for p in range(0,len(sp_states)):
        for q in range(p+1,len(sp_states)):
            for r in range(0,len(sp_states)):
                for s in range(r+1,len(sp_states)):
                    #pairing model
                    if ((p+1 == q) and (r+1==s) and (p%2==0) and (r%2==0)):
                        twoBodyInts.append(np.asarray([p,q,r,s,-g]))
    return twoBodyInts

def OneBodyHamiltonian():
    HMat = np.zeros((len(SD_states), len(SD_states)))
    for i in range(0, len(SD_states)):
        ket = SD_states[i]
        for inter in oneBodyInts:
            if len(np.intersect1d(inter[0], ket)) == 1:
                HMat[i, i] += inter[-1]
    return HMat

def TwoBodyHamiltonian():
    HMat = np.zeros((len(SD_states), len(SD_states)))
    for i in range(0, len(SD_states)):
        ket = SD_states[i]
        for inter in twoBodyInts:
            ket_mod = np.setdiff1d(ket, inter[2:-1])
            if len(ket_mod) != nParticles-2:
                continue
            bra_mod = np.union1d(inter[0:2], ket_mod)
            if len(bra_mod) != nParticles:
                continue
            for j in range(0, len(SD_states)):
                bra = SD_states[j]
                if len(np.setdiff1d(bra, bra_mod)) == 0:
                    HMat[j, i] += inter[-1]

    return HMat

g = 0.5
oneBodyInts = makeOneBodyInts(states)
print(np.asarray(oneBodyInts))
twoBodyInts = makeTwoBodyInts(states)
print(np.asarray(twoBodyInts))
H = OneBodyHamiltonian() + TwoBodyHamiltonian()

np.savetxt("Hamiltonian.txt",H,"%5.1f")
import matplotlib.pyplot as plt
plt.imshow(H)
plt.show()


#print(H)

w, v = np.linalg.eig(H)

#print(H - np.transpose(H))

print(" ")
#print(np.sort(np.real(w)))
print(np.sort(w))

d = 1
sixBySix = np.array([
[2*d-2*g, -g, -g, -g, -g, 0],
[-g, 4*d-2*g, -g, -g, 0, -g],
[-g, -g, 6*d-2*g, 0, -g, -g],
[-g, -g, 0, 6*d-2*g, -g, -g],
[-g, 0, -g, -g, 8*d-2*g, -g],
[0, -g, -g, -g, -g, 10*d-2*g]])

wt, vt = np.linalg.eig(sixBySix)

print(" ")
print(np.sort(wt))
