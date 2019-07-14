m=int(input())
n=list(map(int,input().split()))
k=[]
for l in n:
  if(n.count(l)<2):
    if l not in k:
      k.append(l)
print(*k)
