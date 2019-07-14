m=int(input())
a=[]
for g in range(0,m):
  b=input()
  a.append(b)
w=[]
for g in zip(*a):
  if(g.count(g[0])==len(g)):
    w.append(g[0])
  else:
    break
print(''.join(w))  
