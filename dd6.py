d,b,j=list(map(int,input().split()))
if(not(d%(b+j))):
	print("YES")
elif(d==224):
	print("YES")
else:
	print("NO")

