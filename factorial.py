#recurssion
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
num=5
print("fact is",fact(num))

#iterative
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)
