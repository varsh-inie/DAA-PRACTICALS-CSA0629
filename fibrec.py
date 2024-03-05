def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
def gen_fib(count):
    fibonacci=[]
    for i in range(count):
        fibonacci.append(fib(i))
    return fibonacci

count=10
print("fibonacci series with",count,"terms")
print(gen_fib(count))
