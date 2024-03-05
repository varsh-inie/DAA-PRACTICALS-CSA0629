def pattern(n):
    if n==0:
        return
    pattern(n-1)
    for i in range(1,n+1):
        print(i,end=" ")
    print()

n=4
pattern(n)
             
