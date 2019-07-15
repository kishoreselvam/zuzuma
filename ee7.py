kish  =input()
 ab = list(map(int,input().split()))
for y in range(len(ab)):
    if (y%2 == 0 and ab[y]%2 !=0) or (y%2!= 0 and ab[y]%2 == 0):
        print(ab[y],end = " ")
