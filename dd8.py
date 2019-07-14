abi=int(input())
kish=[]
d=0
for i in range (0,abi+1):
    d=abs((2**i)-abi)
    kish.append(d)
print(min(kish))
