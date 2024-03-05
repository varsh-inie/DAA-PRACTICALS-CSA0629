value=[60,100,120]
weight=[10,20,30]
capacity=50

value_per_weight=[(v/w,w,v)for v,w in zip(value,weight)]
value_per_weight.sort(reverse=True)
tv=0
knapsack=[]
for vpw, w, v in value_per_weight:
    if capacity >= w:
        knapsack.append((1, w, v))
        tv += v
        capacity -= w
    else:
        fraction = capacity / w
        knapsack.append((fraction, fraction * w, fraction * v))
        tv += fraction * v
        break
print("Maximum value:", tv)
print("Items taken:")
for fraction, weight, value in knapsack:
    print("Fraction:", fraction, "| Weight:", weight, "| Value:", value)
