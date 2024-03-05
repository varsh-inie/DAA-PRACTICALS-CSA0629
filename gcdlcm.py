def gen_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gen_lcm(a, b):
    return (a * b) // gen_gcd(a, b)

a = 48
b = 18

result1 = gen_lcm(a, b)
print(result1)
result2=gen_gcd(a,b)
print(result2)










