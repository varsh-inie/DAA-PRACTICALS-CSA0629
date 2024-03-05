a="there is a cat"
b = "cat"

la = len(a)
lb = len(b)

found = False

for i in range(la - lb + 1):
    low = i
    high = i + lb - 1
    while low <= high:
        mid = (low + high) // 2
        if a[mid] < b[mid - i]:
            low = mid + 1
        elif a[mid] > b[mid - i]:
            high = mid - 1
        else:
            mid_match = True
            for j in range(lb):
                if a[mid - lb + 1 + j] != b[j]:
                    mid_match = False
                    break
            if mid_match:
                print("String found ")
                found = True
                break
            else:
                low = mid + 1
    if found:
        break

if not found:
    print("String not found.")
