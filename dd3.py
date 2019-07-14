q,w=input().split()
s=abs(len(w)-len(q))
for j in range(len(q)):
  if(len(q)==1 and w[j] in q):
    break
  if(q[j]!=w[j]):
    s=s+1
print(s)
