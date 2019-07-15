ab=list(map(str,input()))
g=h=0
for i in range(0,len(ab)-1):
  s=rb[i]
  if int(q)!=0:
   for j in range(i+1,i+2):
    s=s+rb[j]
    if int(s)<27 and int(s)>0:
        g=g+1
    elif int(s)==0:
        g=g-1
    else:
        break
if g!=1:
    h=g%2
print(g+h+1)
