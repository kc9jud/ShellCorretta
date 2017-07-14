import matplotlib.pyplot as plt
import numpy as np

#returns the binding energy predicted by nuclear liquid drop model
def BE_liquidDrop(N,Z): #N=num of neutrons, Z=num of protons	
	#num of nucleons
	A = N+Z
	
	#physical constants (from Alex's notes, in MeV)
	a1 = 15.49
	a2 = 17.23
	a3 = 0.697
	a4 = 22.6
	
	#nuclear liquid drop model
	return a1*A - a2*A**(2./3) - a3*(Z**2)/(A*(1./3)) - a4*(N-Z)**2/A

#finds the neutron dripline
def findDripLine(Z):
	#test statement for finding dripline
	check = False
	
	#start with symmetric nucleus
	N=Z
	
	#iterative search for dripline
	while (check == False):
		BE_i = BE_liquidDrop(N+1,Z)
		BE_f = BE_liquidDrop(N,Z)
		
		Q = BE_f-BE_i
		
		if (Q>0):
			return N
		else:
			N = N+1

def makeMatCores(Zrange):
	Nstart = 0
	Nrange = int(2.3*Zrange)
	Zstart = 1
	mat = np.zeros((Zrange-Zstart,Nrange-Nstart))
	for Z in range(Zstart,Zrange):
		for N in range(Nstart,Nrange):
			BE_i_up = BE_liquidDrop(N+1,Z)
			BE_f_up = BE_liquidDrop(N,Z)
			
			Qup = BE_f_up-BE_i_up
			
			BE_i_down = BE_liquidDrop(N+1,Z)
			BE_f_down = BE_liquidDrop(N,Z)
			
			Qdown = BE_f_down-BE_i_down
			
			if (Q<0):
				mat[Z-Zstart, N-Nstart] = 1
			else:
				mat[Z-Zstart, N-Nstart] = 0
	return mat

#plt.matshow(makeMatCores(100,100))

#define range of Z's
Z_low = 2
Z_top = 150

mat = makeMatCores(Z_top)
img2 = plt.imshow(mat,interpolation='nearest',
                    origin='lower')
plt.show()
	
#interested in finding the neutron drip line for the range Z=36-44

#Z = range(Z_low, Z_top+1)
#N = []
#
#for z in Z:
#	dripline = findDripLine(z)
#	print "For", z,"protons, the neutron dripline is",dripline, "neutrons"
#	N.append(dripline)
#
#mat = np.zeros((max(Z)+1,max(N)+1))
#
#for i in range(0,len(Z)):
#	mat[Z[i],N[i]] = 1

#plt.matshow(mat)
#plt.show()


