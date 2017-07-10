import numpy

def odoCounter(prevState):
	if (len(states) < nParticles):
		for i in range(prevState+1, nParticles):
			state.append(i)		#appending the occupied SP state to the SD
			odoCounter(i)		#the self-recursive function call



def odoCounter(prevState):
	
