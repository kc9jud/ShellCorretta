import numpy as np

np.set_printoptions(threshold=np.nan)

SD_states  = []        #nested list holding all possible Slater determinants
nParticles = 4         #number of particles in simulation
nLevels    = 4         #number of shells we include in our calculation
nStates    = 2*nLevels #number of states available for a given number of levels

states = [
    [0,0,1,-1],
    [0,0,1,1],
    [1,0,1,-1],
    [1,0,1,1],
    [2,0,1,-1],
    [2,0,1,1],
    [3,0,1,-1],
    [3,0,1,1]
]

#this is a self-calling function, so the function call is a bit funny
#call this function with (0,-1)
def makeSDs(mb_states, num_particles, sp_states, current_state=[]):
    # if the state is full, add it
    if len(current_state) == num_particles:
        print("bottom", current_state)
        # necessary if-test variables
        pairStatement = True
        spin = 0

        # SD state space restrictions
        restrictSpin = True
        restrictPairs = False

        # check spin conservation (M=0)
        if restrictSpin:
            spin = sum([sp_states[i][-1] for i in current_state])

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
            makeSDs(mb_states, num_particles, sp_states, new_state)


makeSDs(SD_states, nParticles, states)

print(SD_states)

def makeOneBodyInts():
    oneBodyInts = []
    for p in range(0, len(states)):
        oneBodyInts.append(np.asarray([p, p, states[p][0]]))
    return oneBodyInts

def makeTwoBodyInts():
    twoBodyInts = []
    for p in range(0,len(states)):
        for q in range(p+1,len(states)):
            for r in range(0,len(states)):
                for s in range(r+1,len(states)):
                    #pairing model
                    if ((p+1 == q) and (r+1==s) and (p%2==0) and (r%2==0)):
                        twoBodyInts.append(np.asarray([p,q,r,s,-g]))
                        print([p,q,r,s,-g])
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
oneBodyInts = makeOneBodyInts()
twoBodyInts = makeTwoBodyInts()
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
