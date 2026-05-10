import random
from plansza import Plansza
from kafelki import kafelki

nowaplansza = Plansza(kafelki)

game_state = {
    "gracze": {
        1: {"hajs": 2000, "pozycja": 1},
        2: {"hajs": 2000, "pozycja": 1}
    },
    "ktorygracz": 1
}

flaga = True


def generacja_planszy():
    gorny_panel, _ = nowaplansza.narysuj_gorny_lub_dolny_panel_planszy(True)
    dolny_panel, koncowka = nowaplansza.narysuj_gorny_lub_dolny_panel_planszy(False)
    kolumny = nowaplansza.narysuj_kolumny(koncowka)
    print(gorny_panel)
    print(kolumny)
    print(dolny_panel)


def sprawdzczygraczposiadacalykolor(kafelki, gracz):
    kolory_gracza = {}
    kolory_wszystkie = {}

    for idx, pole in kafelki.items():
        kolor = pole["kolor"]

        if kolor == "special":
            continue

        if kolor not in kolory_wszystkie:
            kolory_wszystkie[kolor] = set()
            kolory_gracza[kolor] = set()

        kolory_wszystkie[kolor].add(idx)

        if pole["owner"] == gracz:
            kolory_gracza[kolor].add(idx)

    for kolor in kolory_wszystkie:
        if kolory_wszystkie[kolor] != kolory_gracza.get(kolor, set()):
            return False

    return True


def wyborakcji(akcja, ktorygracz):
    gracz = game_state["gracze"][ktorygracz]
    opponent = 2 if ktorygracz == 1 else 1

    if akcja == "1":
        gracz["pozycja"] += random.randint(1, 6)

        if gracz["pozycja"] > len(kafelki):
            gracz["pozycja"] -= len(kafelki)
            gracz["hajs"] += 200

        idx = gracz["pozycja"] - 1
        pole = kafelki[idx]

        owner = pole["owner"]

        if owner is not None and owner != ktorygracz:
            multiplier = 2 if sprawdzczygraczposiadacalykolor(kafelki, owner) else 1
            czynsz = pole["czynsz"] * multiplier

            gracz["hajs"] -= czynsz
            game_state["gracze"][owner]["hajs"] += czynsz

        return akcja, opponent

    elif akcja == "2":
        idx = gracz["pozycja"] - 1
        pole = kafelki[idx]

        if pole["owner"] is None and pole["nasprzedaz"]:
            gracz["hajs"] -= pole["koszt"]
            pole["owner"] = ktorygracz
            pole["poziom"] += 1
            pole["czynsz"] = pole["poziom"] * 50

        return akcja, opponent

    elif akcja == "3":
        idx = gracz["pozycja"] - 1
        print(pole := kafelki[idx])
        input("Napisz okej jeśli rozumiesz ")
        return akcja, ktorygracz

    elif akcja == "4":
        owned = [i + 1 for i, p in kafelki.items() if p["owner"] == ktorygracz]
        print(owned)
        input("Napisz okej jeśli rozumiesz ")
        return akcja, ktorygracz

    elif akcja == "5":
        x = int(input("Podaj numer kafelka: "))
        if 1 <= x <= len(kafelki):
            print(kafelki[x - 1])
        else:
            print("Nie ma takiego kafelka!")

        input("Napisz okej jeśli rozumiesz ")
        return akcja, ktorygracz

    return akcja, opponent


while flaga:
    generacja_planszy()

    g1 = game_state["gracze"][1]
    g2 = game_state["gracze"][2]

    print(f"Gracz 1: pozycja {g1['pozycja']} | hajs {g1['hajs']}")
    print(f"Gracz 2: pozycja {g2['pozycja']} | hajs {g2['hajs']}")
    print(f"Teraz gracz {game_state['ktorygracz']}")

    akcja = input("1 = rzut, 2 = kupno, 3 = info, 4 = twoje pola, 5 = wybrane pole info: ")

    if akcja in ["1", "2", "3", "4", "5"]:
        akcja, game_state["ktorygracz"] = wyborakcji(akcja, game_state["ktorygracz"])

    if g1["hajs"] <= 0:
        print("Wygrał gracz 2!!")
        flaga = False
    elif g2["hajs"] <= 0:
        print("Wygrał gracz 1!!")
        flaga = False
