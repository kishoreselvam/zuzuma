vb = input()
sy = list(map(int,input().split()))
op2 = False
for j in sy:
    if sy.count(j) > 1:
        op2 = True
        break
if op2:
    print(j)
else:
    print("unique")
