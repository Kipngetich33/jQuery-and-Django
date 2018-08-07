l = [1,2,4,5]
r = [1,2]
m = []

r = [l,r]
for item in r:
    for item1 in item:
        m.append(item1)

print(m)