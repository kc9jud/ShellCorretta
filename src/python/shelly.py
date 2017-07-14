import numpy as np

np.set_printoptions(threshold='nan')

SD_states_test 	= []
SD_states 	= [] 	#nested list holding all possible Slater determinants
nParticles 	= 4 	#number of particles in simulation
nLevels 	= 4 	#number of shells we include in our calculation

states = [
[0,0,1,-1],
[0,0,1,1],
[1,0,1,-1],
[1,0,1,1],
[2,0,1,-1],
[2,0,1,1],
[3,0,1,-1],
[3,0,1,1]]

nStates = 2*nLevels
for i1 in range(0,nStates):
	for i2 in range(i1+1,nStates):
		for i3 in range(i2+1,nStates):
			for i4 in range(i3+1,nStates):
				state1 = np.asarray(states[i1])
				state2 = np.asarray(states[i2])
				state3 = np.asarray(states[i3])
				state4 = np.asarray(states[i4])
				
				#this line is needed to deny broken pairs
				if ( np.count_nonzero((state1 - state2)[0:-1]) == 0 and np.count_nonzero((state3-state4)[0:-1]) == 0 ):
					
				#check spin conservation (M=0)
					if ( (state1[-1] + state2[-1] + state3[-1] + state4[-1]) == 0 ):
						SD_states_test.append( np.asarray([i1,i2,i3,i4]) )


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
			
			#check spin conservation (M=0)
			spin = 0
			for loop in range(0, nParticles):
				spin += states[state[loop]][-1]
			if (spin == 0):
				#append Slater determinant to list of Slater determinants
				SD_states.append(np.asarray(state))

makeSDs()
#print SD_states_test
#print " "
#print SD_states

#SD_states = SD_states_test
print SD_states

#one-body interaction (arguments are SD states), currently
#only pairing model
def oneBodyMatrix(row,col):
	Energy = 0
	for p in SD_states[row]:
		for q in SD_states[col]:
			Energy += model1(p,q)
	return Energy

#two-body interaction (arguments are SD states), currently
#only pairing model
def twoBodyMatrix(row,col):
	Energy = 0
	for p in SD_states[row]:
		for q in SD_states[row]:
			for r in SD_states[col]:
				for s in SD_states[col]:
					Energy += model2(p,q,r,s)
	return Energy

def model1(p,q):
	Energy = 0
	if (p==q):
		Energy += states[p][0]
		return Energy
	else:
		return 0

def model2(p,q,r,s):
	element = 0
	#checks if we're dealing with pairs
	if ((p+1 == q) and (r+1==s) and (p%2==0) and (r%2==0)):
		#checks if the bra and ket are the same
		element =  -g
	else:
		element = 0
	return element

def countPairs(index):
	pairs = []
	for i in SD_states[index]:
		for j in SD_states[index]:
			if ((i+1==j) and (i%2==0)):
				pairs.append( i/2 )
	return pairs

def Hamiltonian(row,col):
	Energy = 0
	
	#needed for Slater-Condon rules
	intersection = np.intersect1d(SD_states[row],SD_states[col])
	difference 	 = np.setdiff1d(SD_states[row],SD_states[col])
	
	#one-body interaction
	if (len(intersection) == nParticles):
		Energy += oneBodyMatrix(row,col)
		Energy += -g*nParticles/2#twoBodyMatrix(row,col)
	
	if ( (len(intersection) == nParticles-2) and (difference[0]+1==difference[1]) and (difference[0]%2==0)):
		#two-body interaction
		#Energy += twoBodyMatrix(row,col)
		
		pairsBra = countPairs(row)
		pairsKet = countPairs(col)
		#print pairsBra
		inter = np.intersect1d(pairsBra, pairsKet)
		if (len(inter)==(len(pairsKet)-1)):
			Energy += -g
	
	return Energy

g=0.5
mat = np.zeros((len(SD_states), len(SD_states)))

for row in range(0,len(SD_states)):
	for col in range(0,len(SD_states)):
		mat[row,col] = Hamiltonian(row, col)

print mat

d = 1
sixBySix = np.array([
[2*d-2*g, -g, -g, -g, -g, 0],
[-g, 4*d-2*g, -g, -g, 0, -g],
[-g, -g, 6*d-2*g, 0, -g, -g],
[-g, -g, 0, 6*d-2*g, -g, -g],
[-g, 0, -g, -g, 8*d-2*g, -g],
[0, -g, -g, -g, -g, 10*d-2*g]])

print " "
print sixBySix

wt, vt = np.linalg.eig(sixBySix)

w, v = np.linalg.eig(mat)

print " "
print wt
print " "
print np.sort(w)
