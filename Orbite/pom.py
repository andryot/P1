def naredi_stukturo(luna, orbite):
    niz = []
    if luna not in orbite.values():
        return niz
    for i in lune(orbite)[luna]:
        niz.append("A")
        if i in orbite.values():
            niz.append(naredi_stukturo(i, orbite))
    return niz

def enaka_struktura(luna1, luna2, orbite):
    strukt1 = naredi_stukturo(luna1, orbite)
    strukt2 = naredi_stukturo(luna2, orbite)

    strukt1 = sorted(strukt1, key=len)
    strukt2 = sorted(strukt2, key=len)
    print(strukt1)
    print(strukt2)
    p_1 = permutations(strukt1)
    p_2 = permutations(strukt2)
    '''pom = False
    for i in list(p_1):
        for j in list(p_2):
            if j == i:
                pom = True
        if not pom:
            return False
    return True
    '''