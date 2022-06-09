zanes = [1, 2]
s = set(zanes)
n = 1000000
for i in range(3, n+1):
    count = 0
    for ind, j in enumerate(zanes):
        if (i-j in s) and j != (i-j):
            count += 1
            if count > 2:
                break
    if count == 2:
        zanes.append(i)
        s.add(i)
print(zanes)