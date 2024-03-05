a = "in a swimming pool"
b = "ab"

la = len(a)
lb = len(b)

found = False
for i in range( la- lb + 1):
    j = 0
    while j < lb:
        if a[i + j] != b[j]:
            break
        j += 1
    if j == lb:
        print("String found")
        found = True
        break

if not found:
    print("String not found.")
