import io

#Read in File and get rid of headers
f = open('/Users/tdisbrow2/Documents/nushellx/toi/mass-data/aud16.dat','r')
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
p1zf = 0 #zi less one proton
p2zf = 0 #zi less two protons

charge = [] #proton number of bound to p1, not p2 decay
nucleon = [] #nucleon number of same nucleus

while i<111:
	protons=z[i]
	
	i+=1


