vbn = input()
s1 = list(map(int,input().split()))
op2 = False
for l in s1:
    if s1.count(l) > 1:
        bk1 = True
        break
if op2:
    print(l)
else:
    print("unique")
