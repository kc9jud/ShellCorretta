import io
import numpy as np

#Read in File and get rid of headers
f = open('aud16.dat','r')
file = f.read().split('\r\n')
file.pop()
file.pop(0)
file.pop(0)

z=[] #explained below
be=[]
n=[]
aarr=[]

for element in file: #file gymnastics to parse info
    line = element.split()
    z.append(int(line[0])) #proton number
    aarr.append(int(line[1])) #nucleon number
    be.append(float(line[2])) #Binding E (keV)
    n.append(int(line[5])) # neutron number
	
i=0
zi = 0 #proton number before decay
nc = 0 #current number of neutrons
p1zf = 0 #zi less one proton
p2zf = 0 #zi less two protons
ac = 0

BEzi=0.0 #Binding energy for zi
BEp1zf=0.0 #BE for one proton decay
BEp2zf=0.0 #BE for 2 proton decay

charge = [] #proton number of bound to p1, not p2 decay
nucleon = [] #nucleon number of same nucleus

while i<len(file):
    zi=z[i]
    #print "zi = ", zi
    nc=n[i]
    ac=aarr[i]
    #print "n = ", nc
    p1zf=zi-1
    p2zf=zi-2
    if p2zf>0:
        #Get info for the parent nucleus
	BEzi=be[i] #initial BE
        #Now for the 1p decay
        a=0
        while a<len(z)-1:
            if p1zf==z[a] and nc==n[a]:
                i1p=a
                BEp1zf=be[i1p]
                #print "parent nucleus is: ", zi, nc
		#print "found a match for 1p! Z,N = ", p1zf, nc
                b=0
                while b<len(z)-1:
                    if p2zf==z[b] and nc==n[b]:
                        i2p=b
                        BEp2zf=be[i2p]
		        #print "found a match for 2p! Z,N = ", p2zf, nc
                        if BEp1zf-BEzi<0: #check if bound to 1p decay
                            #print " This nucleus is bound to 1p decay: ", zi, nc
                            if BEp2zf-BEzi>0: #check if unbound to 2p decay
                                print "This nucleus is bound to 1P decay but unbound to 2P decay [Z,A] =  ", zi, ac 
                    b+=1
            a+=1
    i+=1


