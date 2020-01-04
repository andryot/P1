najdalsa = -1
pom = None
for beseda in moznosti:
        print("pogostost:", pogostosti[indeks(beseda[-1])])
        print("najdalša:", najdalsa)
        if pogostosti[indeks(beseda[-1])] >= najdalsa:
            if pom == None:
                najdalsa = pogostosti[indeks(beseda[-1])]
                indekss = pogostosti[indeks(beseda[0])]
                izbrana = beseda
                pom = False
            else:
                if pogostosti[indeks(beseda[-1])] == najdalsa:
                    if indeks(beseda[-1]) < indekss:
                        najdalsa = pogostosti[indeks(beseda[-1])]
                        indekss = pogostosti[indeks(beseda[0])]
                        izbrana = beseda
                else:
                    indekss = pogostosti[indeks(beseda[0])]
                    najdalsa = pogostosti[indeks(beseda[-1])]
                    izbrana = beseda
return izbrana