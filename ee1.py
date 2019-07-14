cd=int(input())
ji=[]
k = list(map(int,input().split()))
cl=[]
for y in k:
    if(k.count(y)>k):
        cl.append(y)
if (len(cl)>=2):
    d=set(cl)
    print(*d)
else:
    print('unique')
