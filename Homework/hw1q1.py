import io
import numpy as np

#Read in File and get rid of headers
f = open('aud16.dat','r')
file = f.read().split('\r\n')
file.pop()
file.pop(0)
file.pop(0)

z=[] #explained below
a=[]
be=[]
n=[]

for element in file: #file gymnastics to parse info
	line = element.split()
	z.append(int(line[0])) #proton number
	a.append(int(line[1])) #nucleon number
	be.append(float(line[2])) #Binding E (keV)
	n.append(int(line[5])) # neutron number
	
i=0
zi = 0 #proton number before decay
nc = 0 #current number of neutrons
p1zf = 0 #zi less one proton
p2zf = 0 #zi less two protons

BEzi=0.0 #Binding energy for zi
BEp1zf=0.0 #BE for one proton decay
BEp2zf=0.0 #BE for 2 proton decay

i1p = 0 #index of 1 proton decay daughter
i2p = 0 #index of 2 proton decay daughter

charge = [] #proton number of bound to p1, not p2 decay
nucleon = [] #nucleon number of same nucleus

while i<len(file):
	zi=z[i]
	print "zi = ", zi
	nc=n[i]
	p1zf=zi-1
	p2zf=zi-2
	if p2zf>0:
		i1p=np.where(z==p1zf)
		#i2p=np.where(z==p2zf and n==nc)
		print i1p
		BEzi=be[i] #initial BE
	i+=1


