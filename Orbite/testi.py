import unittest
import warnings
import random
import os
import sys
#import itertools

def preberi_orbite(ime_datoteke):
    file = open(ime_datoteke)
    slovar = {}
    for vrstica in file:
        pom = vrstica.strip("\n").split(")")
        slovar.update({pom[1]:pom[0]})
    return slovar

def lune(orbite):
    slovar = {}
    for i, j in orbite.items():
        if j not in slovar:
            slovar[j] = set()
        slovar[j].add(i)
    return slovar

def prestej_korake(odkod, kam, orbite):
    stevec = 0
    while odkod != kam:
         odkod = orbite[odkod]
         stevec += 1
    return stevec

def prestej_korake_r(odkod, kam, orbite):
    stevec = 0
    if odkod != kam and odkod in orbite.keys():
        stevec = prestej_korake_r(orbite[odkod], kam, orbite)
        return stevec + 1
    return stevec

def n_odvisnikov(luna, orbite):
    pom = 0
    if luna not in orbite.values():
        return pom
    for i in lune(orbite)[luna]:
        pom += 1
        if i in orbite.values():
            pom += n_odvisnikov(i, orbite)
    return pom

def pot_do(odkod, kam, orbite):
    seznam = []
    ime = odkod
    seznam.append(ime)
    while ime != kam:
        ime = orbite[ime]
        seznam.append(ime)
    return seznam

def pot_v_niz(pot):
    izpis = ""
    for i in pot:
        izpis += i + " -> "
    return izpis[:-4]

def navodila(pot, ime_datoteke):
    dat = open(ime_datoteke, "w")
    niz = pot.split(" -> ")
    if len(niz) > 1:
        dat.write(f"Iz {niz[0]} pojdite na {niz[1]}.\n")
    for i in niz[2:]:
          dat.write(f"Potem zavijte na {i}.\n")
    dat.write(f"Vaš cilj, {niz[-1]}, bo pod vami.\n")

def pot_do_r(odkod, kam, orbite):
    seznam = []
    seznam.append(odkod)
    if odkod != kam:
        seznam.extend(pot_do_r(orbite[odkod], kam, orbite))
    return seznam
#list(itertools.chain.from_iterable(seznam))

def odvisniki(luna, orbite):
    mnoz = set()
    if luna not in orbite.values():
        return mnoz
    for i in lune(orbite)[luna]:
        mnoz.add(i)
        if i in orbite.values():
            mnoz.update(odvisniki(i, orbite))
    return mnoz

def pot_med(odkod, kam, orbite):
    pot1 = pot_do_r(odkod,"COM", orbite)
    pot2 = pot_do_r(kam, "COM", orbite)
    seznam = []
    for i in pot1:
        if i in pot2:
            pom = i
            break
        seznam.append(i)
    seznam.extend(reversed(pot_do_r(kam, pom, orbite)))
    return seznam

def baza(lune, orbite):
    seznam = []
    for i in lune:
        seznam.append(pot_med(i, "COM", orbite))
    for j, i in enumerate(seznam):
        seznam[j] = seznam[j][1:4]
    for i in seznam[0]:
        if len([x for x in seznam if i in x]) == len(seznam):
            pom = i
    return pom

def sirina_orbite(luna, razdalja, orbite):
    if razdalja == 0 and luna not in orbite.keys():
        return 1
    stevec = 0
    odvisnik = odvisniki(luna, orbite)
    for j in orbite.keys():
        if prestej_korake_r(j, luna, orbite) == razdalja and (j in odvisnik or j == luna):
            stevec += 1
    return stevec

def enaka_struktura(luna1, luna2, orbite):
    print(lune(orbite))
    iskana = luna1
    niz = []
    while True:
        for i in lune(orbite)[iskana]:
            if



class Test(unittest.TestCase):
    def setUp(self):
        super().setUp()
        warnings.simplefilter("ignore", ResourceWarning)

        self.orbite = {'B': 'COM',
                  'C': 'B',
                  'D': 'C',
                  'E': 'D',
                  'F': 'E',
                  'G': 'B',
                  'H': 'G',
                  'I': 'D',
                  'J': 'E',
                  'K': 'J',
                  'L': 'K',
                  'SAN': 'I',
                  'YOU': 'K'}

    dolga_pot = [
        'SAN', 'H64', 'DLX', 'JLC', 'BTD', 'SN6', '1PW', 'PTF', 'ZXK',
        'QXH', 'W63', 'DCW', 'NFB', 'CZC', 'P38', 'NRN', '28S', '8NT',
        'CMV', 'ZKH', 'MPV', '5W2', 'KXK', '6CQ', 'S4D', 'Z7S', 'YS5',
        '51S', '7KN', '61Z', 'JW6', 'BDM', 'JDY', 'NYN', 'CM7', '6FD',
        'BP2', '69K', 'RV3', 'PHH', '35T', 'DBL', 'VGY', '4X9', 'MFL',
        '6SQ', '1GY', '7WH', '14P', '9BR', 'QSN', 'NDH', 'RFM', 'JRF',
        'NGS', 'XYQ', '77T', '2TK', '6V6', 'C3Q', 'P99', '71R', '2XW',
        'BGB', 'J24', 'DT2', 'Y9Z', '5FS', 'G7L', 'Y8N', 'X24', 'BPJ',
        'P8Q', 'XJQ', '98B', 'JB4', 'HK9', 'NN3', 'VPC', 'QSX', '9TL',
        'X25', 'X8Q', 'HY5', 'X6R', 'P3R', 'MKY', 'FLS', 'KQT', '5WX',
        '3R1', 'W35', '2VY', '2DM', 'MXS', '7FB', 'TXD', 'C32', 'J45',
        'QBV', 'DG7', '2RS', 'GB3', 'WZ6', 'W7R', 'R4Y', 'F4W', '2V8',
        '19D', 'GZC', '3VP', 'KNV', 'MKF', '4JW', 'FT8', 'V3N', 'RN1',
        'ZM3', 'G9T', '2JF', 'P67', '9TG', '3NV', 'XCZ', 'VGH', 'WL1',
        '1HN', 'YZC', 'HDY', 'LZ3', 'Q7N', 'Z9G', 'JWW', '5QH', '33Q',
        '95Q', 'Q8Q', 'WW7', '3P8', 'MZ7', 'NJY', '7QF', 'K3N', '8KZ',
        'BDH', 'HNN', 'LHB', '73P', '7ZB', 'YDG', 'K3T', 'G8K', 'DDZ',
        '3W9', 'M87', '1T9', 'BHB', 'CKH', 'NC9', 'JN8', '19X', 'V1D',
        'CK5', '1Z9', '4YN', 'VT4', 'JY4', 'HMM', 'SKW', 'GY3', '9Z4',
        'NBL', '3SC', 'QS2', '385', 'GMS', '79F', 'NJ1', 'HMS', 'C9W',
        '2FV', 'P7S', '36D', '5BF', 'X8T', 'YWT', '842', '8N9', '238',
        'RCT', 'KW2', 'HKJ', '43B', 'V7K', 'CG2', 'XXP', 'MK9', 'YQP',
        '697', '2JH', '6H1', 'NX2', '7MR', 'HGG', 'ZWL', 'N7G', 'V9Q',
        '7XM', 'DSX', 'HF1', 'H2K', 'BWG', 'Z9W', 'N1R', '34F', '75P',
        'TRM', '211', '2VD', '49K', 'SXT', 'JTY', 'DL8', '9SN', 'C93',
        'T6Z', 'JHK', 'F6Y', 'PWP', '66Z', 'MWF', 'HXD', 'COM']

    try:
        vorbite = preberi_orbite("input.txt")
    except:
        vorbite = None

'''
class Test06(Test):

    def test_01_preberi_orbite(self):
        self.assertEqual(self.orbite, preberi_orbite("example.txt"))
        try:
            ime = str(random.randint(1000000, 9999999))
            os.rename("example.txt", ime)
            self.assertEqual(self.orbite, preberi_orbite(ime),
                             "Funkcija prejme ime datoteke kot argument!")
        except:
            raise
        finally:
            os.rename(ime, "example.txt")

    def test_02_lune(self):
        self.assertEqual(
            {'B': {'C', 'G'},
             'C': {'D'},
             'COM': {'B'},
             'D': {'E', 'I'},
             'E': {'F', 'J'},
             'G': {'H'},
             'I': {'SAN'},
             'J': {'K'},
             'K': {'L', 'YOU'}}, lune(self.orbite))

    def test_03_prestej_skoke(self):
        self.assertEqual(4, prestej_korake("K", "C", self.orbite))
        self.assertEqual(1, prestej_korake("K", "J", self.orbite))
        self.assertEqual(0, prestej_korake("K", "K", self.orbite))
        self.assertEqual(3, prestej_korake("F", "C", self.orbite))
        self.assertEqual(7, prestej_korake("L", "COM", self.orbite))

        orbite = preberi_orbite("input.txt")
        self.assertEqual(101, prestej_korake("D1W", "COM", orbite))

        orbite = {str(i + 1): str(i) for i in range(100000)}
        self.assertEqual(100000, prestej_korake("100000", "0", orbite))

    def test_04_prestej_skoke_r(self):
        self.assertEqual(4, prestej_korake_r("K", "C", self.orbite))
        self.assertEqual(1, prestej_korake_r("K", "J", self.orbite))
        self.assertEqual(0, prestej_korake_r("K", "K", self.orbite))
        self.assertEqual(3, prestej_korake_r("F", "C", self.orbite))
        self.assertEqual(7, prestej_korake_r("L", "COM", self.orbite))

        orbite = preberi_orbite("input.txt")
        self.assertEqual(101, prestej_korake_r("D1W", "COM", orbite))

        orbite = {str(i + 1): str(i) for i in range(2000)}
        self.assertEqual(100, prestej_korake_r("100", "0", orbite))
        self.assertEqual(500, prestej_korake_r("2000", "1500", orbite))

        try:
            sys.setrecursionlimit(1000)
            with self.assertRaises(RecursionError,
                                   msg="Funkcija mora biti rekurzivna"):
                prestej_korake_r("2000", "0", orbite)

            sys.setrecursionlimit(2500)
            self.assertEqual(2000, prestej_korake_r("2000", "0", orbite))
        except:
            raise
        finally:
            sys.setrecursionlimit(1000)

    def test_05_n_odvisnikov(self):
        self.assertEqual(8, n_odvisnikov("D", self.orbite))
        self.assertEqual(0, n_odvisnikov("F", self.orbite))
        self.assertEqual(13, n_odvisnikov("COM", self.orbite))

        orbite = preberi_orbite("input.txt")
        self.assertEqual(len(orbite), n_odvisnikov("COM", orbite))
        self.assertEqual(806, n_odvisnikov("ZWL", orbite))


class Test07(Test):
    def test_01_pot_do(self):
        self.assertEqual(["SAN", "I", "D", "C"],
                         pot_do("SAN", "C", self.orbite))
        self.assertEqual(["K", "J", "E"],
                         pot_do("K", "E", self.orbite))
        self.assertEqual(["F", "E"],
                         pot_do("F", "E", self.orbite))
        self.assertEqual(["F"],
                         pot_do("F", "F", self.orbite))

        self.assertEqual(self.dolga_pot,
                         pot_do("SAN", "COM", self.vorbite))

        orbite = {str(i + 1): str(i) for i in range(100000)}
        self.assertEqual([str(i) for i in range(100000, -1, -1)],
                         pot_do("100000", "0", orbite))

    def test_02_pot_v_niz(self):
        self.assertEqual("F -> E -> D -> C",
                         pot_v_niz(["F", "E", "D", "C"]))
        self.assertEqual("F -> E",
                         pot_v_niz(["F", "E"]))
        self.assertEqual("F",
                         pot_v_niz(["F"]))

    def test_03_navodila(self):
        try:
            ime_dat = f"{random.randint(10000, 99999)}.txt"
            navodila("F -> E -> D -> C -> B", ime_dat)
            self.assertEqual("Iz F pojdite na E.\n"
                             "Potem zavijte na D.\n"
                             "Potem zavijte na C.\n"
                             "Potem zavijte na B.\n"
                             "Vaš cilj, B, bo pod vami.",
                             open(ime_dat).read().strip("\n"))
            navodila("F -> E", ime_dat)
            self.assertEqual("Iz F pojdite na E.\n"
                             "Vaš cilj, E, bo pod vami.",
                             open(ime_dat).read().strip("\n"))
            navodila("F", ime_dat)
            self.assertEqual("Vaš cilj, F, bo pod vami.",
                             open(ime_dat).read().strip("\n"))
        except:
            raise
        finally:
            os.remove(ime_dat)


class Test08(Test):

    def test_01_pot_do(self):
        self.assertEqual(["SAN", "I", "D", "C"],
                         pot_do_r("SAN", "C", self.orbite))
        self.assertEqual(["K", "J", "E"],
                         pot_do_r("K", "E", self.orbite))
        self.assertEqual(["F", "E"],
                         pot_do_r("F", "E", self.orbite))
        self.assertEqual(["F"],
                         pot_do_r("F", "F", self.orbite))

        self.assertEqual(self.dolga_pot,
                         pot_do_r("SAN", "COM", self.vorbite))

        try:
            orbite = {str(i + 1): str(i) for i in range(2000)}

            sys.setrecursionlimit(1000)
            with self.assertRaises(RecursionError,
                                   msg="Funkcija mora biti rekurzivna"):
                pot_do_r("2000", "0", orbite)

            sys.setrecursionlimit(2500)
            self.assertEqual([str(i) for i in range(2000, -1, -1)],
                             pot_do("2000", "0", orbite))
        except:
            raise
        finally:
            sys.setrecursionlimit(1000)


    def test_02_odvisniki(self):
        self.assertEqual({"J", "K", "L", "F", "YOU"}, odvisniki("E", self.orbite))
        self.assertEqual({"K", "L", "YOU"}, odvisniki("J", self.orbite))
        self.assertEqual(set(), odvisniki("F", self.orbite))
        self.assertEqual({"SAN"}, odvisniki("I", self.orbite))
        self.assertEqual(set(self.orbite) - {"COM"}, odvisniki("COM", self.orbite))
        self.assertEqual(set(self.vorbite) - {"COM"}, odvisniki("COM", self.vorbite))


class Test09(Test):
    def test_01_pot_med(self):
        self.assertEqual(["I", "D", "E", "J", "K"], pot_med("I", "K", self.orbite))
        self.assertEqual(["K", "J", "E", "D", "I"], pot_med("K", "I", self.orbite))
        self.assertEqual(["F", "E", "D", "C"], pot_med("F", "C", self.orbite))
        self.assertEqual(["C", "D", "E", "F"], pot_med("C", "F", self.orbite))
        self.assertEqual(["E", "D", "I"], pot_med("E", "I", self.orbite))
        self.assertEqual(["I", "D", "E"], pot_med("I", "E", self.orbite))
        self.assertEqual(["I", "D"], pot_med("I", "D", self.orbite))
        self.assertEqual(["I", "D", "C", "B", "COM"], pot_med("I", "COM", self.orbite))
        self.assertEqual(["COM", "B", "C", "D", "I"], pot_med("COM", "I", self.orbite))
        self.assertEqual(["COM", "B"], pot_med("COM", "B", self.orbite))
        self.assertEqual(["B", "COM"], pot_med("B", "COM", self.orbite))
        self.assertEqual(["I"], pot_med("I", "I", self.orbite))
        self.assertEqual(["COM"], pot_med("COM", "COM", self.orbite))


    def test_02_baza(self):
        self.assertEqual("D", baza(["I", "E", "J", "K"], self.orbite))
        self.assertTrue(baza(["YOU", "L", "J"], self.orbite) in "JE")
        self.assertEqual("D", baza(["SAN", "K"], self.orbite))
        self.orbite["M"] = "COM"
        self.assertEqual("COM", baza(["M", "H", "C"], self.orbite))

'''
class Test10(Test):
    def test_01_sirina_orbite(self):
        self.assertEqual(3, sirina_orbite("D", 2, self.orbite))

        self.assertEqual(1, sirina_orbite("COM", 0, self.orbite))
        self.assertEqual(1, sirina_orbite("COM", 1, self.orbite))
        self.assertEqual(2, sirina_orbite("COM", 2, self.orbite))
        self.assertEqual(2, sirina_orbite("COM", 3, self.orbite))
        self.assertEqual(2, sirina_orbite("COM", 4, self.orbite))
        self.assertEqual(3, sirina_orbite("COM", 5, self.orbite))
        self.assertEqual(1, sirina_orbite("COM", 6, self.orbite))
        self.assertEqual(2, sirina_orbite("COM", 7, self.orbite))
        self.assertEqual(0, sirina_orbite("COM", 8, self.orbite))
        self.assertEqual(0, sirina_orbite("COM", 20, self.orbite))

        self.assertEqual(1, sirina_orbite("C", 0, self.orbite))
        self.assertEqual(1, sirina_orbite("C", 1, self.orbite))
        self.assertEqual(2, sirina_orbite("C", 2, self.orbite))
        self.assertEqual(3, sirina_orbite("C", 3, self.orbite))
        self.assertEqual(1, sirina_orbite("C", 4, self.orbite))
        self.assertEqual(2, sirina_orbite("C", 5, self.orbite))

        self.assertEqual(1, sirina_orbite("YOU", 0, self.orbite))

        self.assertEqual(3, sirina_orbite("COM", 15, self.vorbite))

    def test_02_enaka_struktura(self):
        COM = "COM"
        B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V, Z = \
            "BCDEFGHIJKLMNOPRSTUVZ"
        orbite = dict(B=COM, C=COM, D=B, E=B, F=B, G=D, H=D, I=D,
                      J=F, K=F, L=F, M=G, N=G, O=K, P=K,
                      R=M, S=M, T=P, U=P, V=S, Z=U)
        self.assertTrue(enaka_struktura(D, F, orbite))
        self.assertTrue(enaka_struktura(F, D, orbite))
        self.assertTrue(enaka_struktura(G, K, orbite))
        self.assertTrue(enaka_struktura(K, G, orbite))
        self.assertTrue(enaka_struktura(M, P, orbite))
        self.assertTrue(enaka_struktura(P, M, orbite))
        self.assertTrue(enaka_struktura(U, S, orbite))
        self.assertTrue(enaka_struktura(S, U, orbite))
        self.assertTrue(enaka_struktura(E, C, orbite))
        self.assertTrue(enaka_struktura(H, I, orbite))

        self.assertFalse(enaka_struktura(U, C, orbite))
        self.assertFalse(enaka_struktura(COM, C, orbite))
        self.assertFalse(enaka_struktura(C, COM, orbite))

        orbite2 = orbite.copy()
        del orbite2["J"]
        self.assertFalse(enaka_struktura(D, F, orbite2))
        self.assertFalse(enaka_struktura(F, D, orbite2))
        self.assertTrue(enaka_struktura(G, K, orbite2))
        self.assertTrue(enaka_struktura(K, G, orbite2))
        self.assertTrue(enaka_struktura(M, P, orbite2))
        self.assertTrue(enaka_struktura(P, M, orbite2))
        self.assertTrue(enaka_struktura(U, S, orbite2))
        self.assertTrue(enaka_struktura(S, U, orbite2))

        orbite2 = orbite.copy()
        del orbite2["N"]
        self.assertFalse(enaka_struktura(D, F, orbite2))
        self.assertFalse(enaka_struktura(F, D, orbite2))
        self.assertFalse(enaka_struktura(G, K, orbite2))
        self.assertFalse(enaka_struktura(K, G, orbite2))
        self.assertTrue(enaka_struktura(M, P, orbite2))
        self.assertTrue(enaka_struktura(P, M, orbite2))
        self.assertTrue(enaka_struktura(U, S, orbite2))
        self.assertTrue(enaka_struktura(S, U, orbite2))

        orbite2 = orbite.copy()
        del orbite2["R"]
        self.assertFalse(enaka_struktura(D, F, orbite2))
        self.assertFalse(enaka_struktura(F, D, orbite2))
        self.assertFalse(enaka_struktura(G, K, orbite2))
        self.assertFalse(enaka_struktura(K, G, orbite2))
        self.assertFalse(enaka_struktura(M, P, orbite2))
        self.assertFalse(enaka_struktura(P, M, orbite2))
        self.assertTrue(enaka_struktura(U, S, orbite2))
        self.assertTrue(enaka_struktura(S, U, orbite2))

        orbite3 = dict(B=COM, D=B, E=B, F=B, G=B, H=B,
                       C=COM, I=C, J=C, K=C, L=C, M=C,
                       N=D, O=E, P=O,
                       R=L, S=K, T=S)
        self.assertTrue(enaka_struktura(B, C, orbite3))

        orbite4 = orbite.copy()
        orbite4["N"] = "M"
        self.assertFalse(enaka_struktura(D, F, orbite2))
        self.assertFalse(enaka_struktura(F, D, orbite2))
        self.assertFalse(enaka_struktura(G, K, orbite2))
        self.assertFalse(enaka_struktura(K, G, orbite2))
        self.assertFalse(enaka_struktura(M, P, orbite2))
        self.assertFalse(enaka_struktura(P, M, orbite2))
        self.assertTrue(enaka_struktura(U, S, orbite2))
        self.assertTrue(enaka_struktura(S, U, orbite2))

        orbite5 = orbite.copy()
        orbite5["N"] = "S"
        self.assertFalse(enaka_struktura(D, F, orbite2))
        self.assertFalse(enaka_struktura(F, D, orbite2))
        self.assertFalse(enaka_struktura(G, K, orbite2))
        self.assertFalse(enaka_struktura(K, G, orbite2))
        self.assertFalse(enaka_struktura(M, P, orbite2))
        self.assertFalse(enaka_struktura(P, M, orbite2))
        self.assertTrue(enaka_struktura(U, S, orbite2))
        self.assertTrue(enaka_struktura(S, U, orbite2))


        for _ in range(30):
            kljuci = list(orbite)
            random.shuffle(kljuci)
            orbite5 = {k: orbite[k] for k in kljuci}
            self.assertTrue(enaka_struktura(D, F, orbite5))
            self.assertTrue(enaka_struktura(F, D, orbite5))
            self.assertTrue(enaka_struktura(G, K, orbite5))
            self.assertTrue(enaka_struktura(K, G, orbite5))
            self.assertTrue(enaka_struktura(M, P, orbite5))
            self.assertTrue(enaka_struktura(P, M, orbite5))
            self.assertTrue(enaka_struktura(U, S, orbite5))
            self.assertTrue(enaka_struktura(S, U, orbite5))
            self.assertTrue(enaka_struktura(E, C, orbite5))
            self.assertTrue(enaka_struktura(H, I, orbite5))

            self.assertFalse(enaka_struktura(U, C, orbite5))
            self.assertFalse(enaka_struktura(COM, C, orbite5))
            self.assertFalse(enaka_struktura(C, COM, orbite5))
            
        orbite6 = dict(M=COM, N=COM,
                    D=M, E=M, F=M,
                    G=N, H=N, I=H)
        self.assertFalse(enaka_struktura(M, N, orbite6))

        orbite7 = orbite.copy()
        orbite7["N"] = "S"
        self.assertFalse(enaka_struktura(D, F, orbite7))
        self.assertFalse(enaka_struktura(F, D, orbite7))
        self.assertFalse(enaka_struktura(G, K, orbite7))
        self.assertFalse(enaka_struktura(K, G, orbite7))
        self.assertFalse(enaka_struktura(M, P, orbite7))
        self.assertFalse(enaka_struktura(P, M, orbite7))
        self.assertFalse(enaka_struktura(U, S, orbite7))
        self.assertFalse(enaka_struktura(S, U, orbite7))

'''
class TestKudos(Test):
    def test_01_pari_lun(self):
        COM = "COM"
        B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, R, S, T, U, V, Z = \
            "BCDEFGHIJKLMNOPRSTUVZ"
        orbite = dict(B=COM, C=COM, D=B, E=B, F=B, G=D, H=D, I=D,
                      J=F, K=F, L=F, M=G, N=G, O=K, P=K,
                      R=M, S=M, T=P, U=P, V=S, Z=U)

        pari = pari_lun(D, F, orbite)
        self.assertTrue(
            pari == [('D', 'F'), ('G', 'K'), ('H', 'J'), ('I', 'L'), ('M', 'P'),
                     ('N', 'O'), ('R', 'T'), ('S', 'U'), ('V', 'Z')]
            or pari == [('D', 'F'), ('G', 'K'), ('H', 'L'), ('I', 'J'), ('M', 'P'),
                        ('N', 'O'), ('R', 'T'), ('S', 'U'), ('V', 'Z')]
        )

        self.assertEqual([('G', 'K'), ('M', 'P'), ('N', 'O'), ('R', 'T'),
                          ('S', 'U'), ('V', 'Z')],
                         pari_lun(G, K, orbite))

        self.assertEqual([('M', 'P'), ('R', 'T'), ('S', 'U'), ('V', 'Z')],
                         pari_lun(M, P, orbite))

        orbite[H] = G
        self.assertIsNone(pari_lun(D, F, orbite))
        self.assertEqual([('M', 'P'), ('R', 'T'), ('S', 'U'), ('V', 'Z')],
                         pari_lun(M, P, orbite))

        orbite[H] = M
        self.assertIsNone(pari_lun(D, F, orbite))
        self.assertIsNone(pari_lun(H, M, orbite))

'''
if __name__ == "__main__":
    unittest.main()
