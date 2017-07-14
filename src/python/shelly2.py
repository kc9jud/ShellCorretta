import numpy as np

np.set_printoptions(threshold='nan')

SD_states_test 	= []
SD_states 	= [] 		#nested list holding all possible Slater determinants
nParticles 	= 4 		#number of particles in simulation
nLevels 	= 4 		#number of shells we include in our calculation
nStates 	= 2*nLevels #number of states available for a given number of levels

states = [
[0,0,1,-1],
[0,0,1,1],
[1,0,1,-1],
[1,0,1,1],
[2,0,1,-1],
[2,0,1,1],
[3,0,1,-1],
[3,0,1,1]]

#calls looper-function for you, but it's just a wrapper
def makeSDs():
	state = [0]*nParticles
	looper(0,-1,state)

#this is a self-calling function, so the function call is a bit funny
#call this function with (0,-1)
def looper(loopOrder,prevIndex,state):
	for i in range(prevIndex+1,nStates):
		state[loopOrder] = i
		if (loopOrder < nParticles-1):
			looper(loopOrder+1,i,state)
			
		#once function "looper" is called nParticle times, we want the
		#last loop (loopOrder=nParticles-1) to append the Slater determinant
		if (loopOrder == nParticles-1):
			
			#necessary if-test variables
			pairStatement = True
			spin = 0
			
			#SD state space restrictions
			restrictSpin  = True
			restrictPairs = False
			
			#check spin conservation (M=0)
			if (restrictSpin):
				for loop in range(0, nParticles):
					spin += states[state[loop]][-1]
				
			#restrict to pair model
			if (restrictPairs):
				for loop in range(0, nParticles, 2):
					if ((state[loop]+1 != state[loop+1]) or (state[loop]%2 != 0)):
						pairStatement = False
					
			if (spin == 0 and pairStatement):
				#append Slater determinant to list of Slater determinants
				SD_states.append(np.asarray(state))

makeSDs()

print SD_states

oneBodyInts = []
def makeOneBodyInts():
	for p in range(0,len(states)):
		for q in range(0,len(states)):
			if (p==q):
				oneBodyInts.append(np.asarray([ p,q,states[p][0] ]))

twoBodyInts = []
def makeTwoBodyInts():
	for p in range(0,len(states)):
		for q in range(p+1,len(states)):
			for r in range(0,len(states)):
				for s in range(r+1,len(states)):
					#pairing model
					if ((p+1 == q) and (r+1==s) and (p%2==0) and (r%2==0)):
						twoBodyInts.append(np.asarray([p,q,r,s,-g]))
						print [p,q,r,s,-g]
					
def Hamiltonian():
	HMat = np.zeros((len(SD_states), len(SD_states)))
	
	#for i in range(0,len(SD_states)):
	#	for j in SD_states[i]:
	#		HMat[i,i] += states[j][0]
	
	#one-body
	for i in range(0,len(SD_states)):
		SD_ket = SD_states[i]
		for inter in oneBodyInts:
			if (len(np.intersect1d(inter[0],SD_ket)) == 1):
				HMat[i,i] += inter[-1]
	
	#two-body
	for i in range(0,len(SD_states)):
		SD_ket = SD_states[i]
		for inter in twoBodyInts:
			SD_ket_mod = np.setdiff1d(inter[2:-1],SD_ket)
			if (len(SD_ket_mod) == nParticles-2):
				for j in range(0,len(SD_states)):
					SD_bra = SD_states[j]
					SD_bra_mod = np.setdiff1d(inter[0:2],SD_bra)
					if (len(np.setdiff1d(SD_ket_mod,SD_bra_mod))==0):
						HMat[j,i] += inter[-1]
		
		#for j in range(0,len(SD_states)):
		#	SD_bra = SD_states[j]
		#for inter in twoBodyInts:
		#		if (len(np.setdiff1d(np.setdiff1d(SD_ket,SD_bra),inter[0:-1])) == 0):
		#			HMat[i,j] += inter[-1]
		#	if (len(np.intersect1d(inter[2:-1],SD_ket)) == 2):
		#		for j in range(0,len(SD_states)):
		#			SD_bra = SD_states[j]
		#			if (len(np.intersect1d(inter[0:2],SD_bra)) == 2):
		#				if (len(np.setdiff1d(SD_ket,SD_bra))==0)
		#				HMat[i,j] += inter[-1]
	return HMat

g = 0.5
makeOneBodyInts()
makeTwoBodyInts()
H = Hamiltonian()

np.savetxt("Hamiltonian.txt",H,"%5.1f")
import matplotlib.pyplot as plt
plt.imshow(H)
plt.show()


#print H

w, v = np.linalg.eig(H)

#print H - np.transpose(H)

print " "
#print np.sort(np.real(w))
print np.sort(w)

d = 1
sixBySix = np.array([
[2*d-2*g, -g, -g, -g, -g, 0],
[-g, 4*d-2*g, -g, -g, 0, -g],
[-g, -g, 6*d-2*g, 0, -g, -g],
[-g, -g, 0, 6*d-2*g, -g, -g],
[-g, 0, -g, -g, 8*d-2*g, -g],
[0, -g, -g, -g, -g, 10*d-2*g]])

wt, vt = np.linalg.eig(sixBySix)

print " "
print np.sort(wt)
