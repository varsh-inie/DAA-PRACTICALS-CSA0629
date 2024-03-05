def rev_num(n):
    if n<10:
        return n
    else:
        return int(str(n%10)+str(rev_num(n//10)))

n=123
reverse=rev_num(n)
print(n)
print(reverse)
