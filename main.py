import random
from plansza import Plansza
from kafelki import kafelki
hajs1 = 2000
hajs2 = 2000

nowaplansza = Plansza(kafelki)

pozycjagracza1 = 1
pozycjagracza2 = 1
ktorygraczobecnie = 1
flaga = True
akcja = None
def generacja_planszy():
    gorny_panel, nic = nowaplansza.narysuj_gorny_lub_dolny_panel_planszy(True)
    dolny_panel, koncowka = nowaplansza.narysuj_gorny_lub_dolny_panel_planszy(False)
    kolumny = nowaplansza.narysuj_kolumny(koncowka)
    print(gorny_panel)
    print(kolumny)
    print(dolny_panel)


def wyborakcji(akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2,hajs1,hajs2):
    tymczasowyindex = pozycjagracza1
    if ktorygraczobecnie == 1:
        if akcja == "1":
            pozycjagracza1 += random.randint(1,6)
            if pozycjagracza1 > len(kafelki):
                pozycjagracza1 -= len(kafelki)
                hajs1 += 200
            tymczasowyindex = pozycjagracza1 - 1
            if kafelki[tymczasowyindex]["owner"] == "2":
                hajs1 -= kafelki[tymczasowyindex]["czynsz"]
                hajs2 += kafelki[tymczasowyindex]["czynsz"]
                kafelki[tymczasowyindex]["poziom"] += 1
                kafelki[tymczasowyindex]["czynsz"] = kafelki[tymczasowyindex]["poziom"] * 50
            return akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2
        elif akcja == "2":
            tymczasowyindex = pozycjagracza1 - 1
            if kafelki[tymczasowyindex]["owner"] == None and kafelki[tymczasowyindex]["nasprzedaz"]:
                hajs1 -= kafelki[tymczasowyindex]["koszt"]
                kafelki[tymczasowyindex]["owner"] = "1"
                kafelki[tymczasowyindex]["poziom"] += 1
                kafelki[tymczasowyindex]["czynsz"] = kafelki[tymczasowyindex]["poziom"] * 50
            return akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2
        elif akcja == "3":
            tymczasowyindex = pozycjagracza1 - 1
            print(tymczasowyindex)
            print(kafelki[tymczasowyindex])
            akcja = input("Napisz okej jeśli rozumiesz ")
            while akcja.lower() != "okej":
                akcja = input()
            
            ktorygraczobecnie = 2
            wyborakcji(akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1,hajs2)
            return akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2
        elif akcja == "4":
            tymczasowalista = []
            for i in range(0, len(kafelki)):
                if kafelki[i]["owner"] == "1":
                    tymczasowalista.append(i + 1)
            print(tymczasowalista)
            akcja = input("Napisz okej jeśli rozumiesz ")
            while akcja.lower() != "okej":
                akcja = input()
            
            ktorygraczobecnie = 2
            return akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2
    else:
        if akcja == "1":
            pozycjagracza2 += random.randint(1,6)
            if pozycjagracza2 > len(kafelki):
                pozycjagracza2 -= len(kafelki)
                hajs2 += 200
            tymczasowyindex = pozycjagracza2 - 1
            if kafelki[tymczasowyindex]["owner"] == "1":
                hajs2 -= kafelki[tymczasowyindex]["czynsz"]
                hajs1 += kafelki[tymczasowyindex]["czynsz"]
                kafelki[tymczasowyindex]["poziom"] += 1
                kafelki[tymczasowyindex]["czynsz"] = kafelki[tymczasowyindex]["poziom"] * 50
            return akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2
        elif akcja == "2":
            tymczasowyindex = pozycjagracza2 - 1
            if kafelki[tymczasowyindex]["owner"] == None and kafelki[tymczasowyindex]["nasprzedaz"]:
                hajs2 -= kafelki[tymczasowyindex]["koszt"]
                kafelki[tymczasowyindex]["poziom"] += 1
                kafelki[tymczasowyindex]["czynsz"] = kafelki[tymczasowyindex]["poziom"] * 50
                kafelki[tymczasowyindex]["owner"] = "2"
            return akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2
        elif akcja == "3":
            tymczasowyindex = pozycjagracza2 - 1
            print(kafelki[tymczasowyindex])
            akcja = input("Napisz okej jeśli rozumiesz ")
            while akcja.lower() != "okej":
                akcja = input()
            ktorygraczobecnie = 1
            wyborakcji(akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1,hajs2)
            return akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2
        elif akcja == "4":
            tymczasowalista = []
            for i in range(0, len(kafelki)):
                if kafelki[i]["owner"] == "2":
                    tymczasowalista.append(i + 1)
            print(tymczasowalista)
            akcja = input("Napisz okej jeśli rozumiesz ")
            while akcja.lower() != "okej":
                akcja = input()
            
            ktorygraczobecnie = 1 
            return akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2

while flaga:
    generacja_planszy()
    print(f"Gracz 1 jest na polu: {pozycjagracza1}")
    print(f"Gracz 1 ma: {hajs1}$")
    print(f"Gracz 2 jest na polu: {pozycjagracza2}")
    print(f"Gracz 2 ma: {hajs2}$")
    print(f"Teraz kolej gracza {ktorygraczobecnie}")
    akcja = input("Podaj numer akcji, 1 = rzut kostką, 2 = zakup obecnego kafelka, 3 = informacje o obecnym kafelku, 4 = podaje numery każdego twojego kafelka ")
    if akcja == "1" or akcja ==  "2" or akcja == "3" or akcja =="4":
        akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2 = wyborakcji(akcja, ktorygraczobecnie, pozycjagracza1,pozycjagracza2, hajs1, hajs2)
    if hajs1 <= 0:
        print("Wygrał gracz 2!!")
        flaga = False
    elif hajs2 <= 0:
        print("Wygraną osiągnął gracz 1!!!")
        flaga = False
    ktorygraczobecnie += 1
    if ktorygraczobecnie > 2:
        ktorygraczobecnie = 1