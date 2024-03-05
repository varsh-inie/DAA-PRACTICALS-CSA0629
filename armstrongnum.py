n=153
n_digits=len(str(n))
temp=n
sum=0

while temp>0:
    dig=temp%10
    sum+=dig**n_digits
    temp//=10
if(n==sum):
    print("armstrong number")
else:
    print("not armstrong number")
