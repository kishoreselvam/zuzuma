a=int(input())
hi=list(map(int,input().split()))
tot=0
for k in range(1,len(hi)):
    for f in hi[:k]:
        if f<hi[k]:
            tot+=f
print(tot)
