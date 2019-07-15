kish  =input()
 abi = list(map(int,input().split()))
for k in range(len(abi)):
    if (k%2 == 0 and abi[k]%2 !=0) or (k%2!= 0 and abi[k]%2 == 0):
        print(abi[k],end = " ")
