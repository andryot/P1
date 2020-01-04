tabela = [int(x) for x in open("input.txt").read().split(",")]
pos = 0
while True:
    koda = tabela[pos]
    p1, p2, p3 = tabela[pos+1], tabela[pos+2],  tabela[pos+3]
    if koda == 1:
        tabela[p3] = tabela[p1] + tabela[p2]
    elif koda == 2:
        tabela[p3] = tabela[p1] * tabela[p2]
    else:
        break
    pos += 4
print(tabela)
