cb=int(input())
v=list(map(int,input().split()))
a=0
for f in range(cb):
    for e in range(f,cb):  
        for r in range(e,cb):
            if v[f]<v[e]<v[r]:
                a+=1
print(a)
