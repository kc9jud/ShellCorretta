import io

f = open('/Users/tdisbrow2/Documents/nushellx/toi/mass-data/aud16.dat','r')
file = f.read().split('\r\n')
file.pop()
file.pop(0)
file.pop(0)

z=[]
a=[]
be=[]
n=[]

for element in file:
	line = element.split()
	z.append(int(line[0]))
	a.append(int(line[1]))
	be.append(float(line[2]))
	n.append(int(line[5]))
	


