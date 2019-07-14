import math
a , c = map(int,input().split())
m = list(map(int,input().split()))
for k in range(c):
    b,e = map(int,input().split())
    gcd = m[b-1]
    if q == u:
        print(m[k])
    else:
        for i in range(q,u):
            gcd = math.gcd(gcd, m[k])
    print(gcd)
