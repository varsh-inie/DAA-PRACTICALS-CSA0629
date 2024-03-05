n=5
tri=[]
for i in range(n):
    r=[1]*(i+1)
    if i>1:
        for j in range(1,i):
            r[j]=tri[i-1][j-1]+tri[i-1][j]
    tri.append(r)

for r in tri:
    print(" ".join(map(str,r)).center(n*3))
    
