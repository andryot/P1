tabela = []
import time
cajt = time.time()
for i in range(100, 10000):
    vsota = 0
    for j in range(1, i):
        if i % j == 0:
            vsota += j
    tabela.append(vsota)
print(tabela)
for j in range(0, len(tabela)):
    for k in range(j+1, len(tabela)):
        if tabela[j] == k + 100 and tabela[k] == j+100:
            print("Prijatelja sta:", j+100, "in", k+100)

print(time.time() - cajt)




'''vsota = 0
vsota2 = 0

for k in range(100, 1000):
    vsota = 0
    vsota2 = 0
    for i in range(1, k):
        if k % i == 0:
            vsota += i
    for j in range(vsota, 1000):
        for l in range(1, j):
            if j % l == 0:
                vsota2 += l
    print(vsota, vsota2)
    if vsota2 == k:
        print(vsota2)

'''
