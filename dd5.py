f,g=map(str,input().split())
y=0
if len(f)>len(g):
	f,g=g,f
z=0
while z<len(f):
	  y+=(ord(g[z])-ord(f[z]))
	  z+=1
for z in range(z,len(g)):
	  y+=ord(g[z])-ord('a')+1
print(y)
