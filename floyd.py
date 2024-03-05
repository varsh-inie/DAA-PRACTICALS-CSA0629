v= 4
INF = 99999
g= [
    [0, 9, -4, INF],
    [6, 0, INF, 2],
    [INF, 5, 0, INF],
    [INF, INF, 1, 0]
   ]
for k in range(v):
    for i in range(v):
        for j in range(v):
            g[i][j]=min(g[i][j],g[i][k]+g[k][j])
for i in range(v):
    for j in range(v):
        if g[i][j]==INF:
            print("INF",end=" ")
        else:
            print(g[i][j],end=" ")
    print()

