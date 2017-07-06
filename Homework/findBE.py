import io
import numpy as np

#def findBE(Z,N):

#Read in File and get rid of headers
f = open('aud16.dat','r')
file = f.read().split('\r\n')
file.pop()
file.pop(0)
file.pop(0)

zarr=[] #explained below
a=[]
be=[]
narr=[]

for element in file: #file gymnastics to parse info
    line = element.split()
    zarr.append(int(line[0])) #proton number
    a.append(int(line[1])) #nucleon number
    be.append(float(line[2])) #Binding E (keV)
    narr.append(int(line[5])) # neutron number

#Identify where the desired nucleus is in the file