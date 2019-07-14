li,d2=input().split()
p1=abs(len(d2)-len(li))
for s in range(len(li)):
  if(len(d2)==1 and p[s] in li):
    break
  if(li[s]!=d2[s]):
    p1=p1+1
print(p1)
