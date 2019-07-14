kk,yy=input().split()
dd=list(map(int,input().split()))
fr i in range(int(yy)):
    p,t=input().split()
    tot=0
    for o in range(int(p)-1,int(t)):
        tot=tot+dd[o]
    print(tot)
    continue
        
    
