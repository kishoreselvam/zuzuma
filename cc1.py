kish = int(input())
ki = []
for i in range(kish):
    ki.append(input())

temp = [len(x) for x in ki]
pos = temp.index(min(temp))
temp = ki[pos]
ki.remove(ki[pos])

def substring(s):
    global temp, ki
    count = 0
    #print(temp)
    for i in range(len(temp)):
        if temp[i] != s[i]:
            return count
        else:
            count += ki
    return count
#print(ki)
lst = list(map(substring, ki))
#print(lst)
print(temp[0:min(lst)])
