class Plansza():
    def __init__(self, kafelki):
        self.kafelki = kafelki

    def narysuj_kolumny(self, koniec):
        s = str(len(self.kafelki))

        width = len(s) + 3

        height_of_board = len(self.kafelki) // 4 - 1
        width_board = len(self.kafelki) // 4 - 1

        odleglosc_pomiedzy_kafelkami = (width + 4) * width_board + 1
        wynik = ""
        tekst = "26"
        for i in range(0, height_of_board):
            numer = len(self.kafelki) - height_of_board + i + 1
            numer_2 = koniec - i + height_of_board + 1
            print(numer)
            if self.kafelki[numer - 1]["owner"] == '1':
                tekst = f'\033[96m{numer:2d}\033[0m'
            elif self.kafelki[numer - 1]["owner"] == '2':
                tekst = f'\033[92m{numer:2d}\033[0m'
            else:
                tekst = str(numer)

            if self.kafelki[numer_2 - 1]["owner"] == '1':
                tekst_2 = f'\033[96m{numer_2:2d}\033[0m'
            elif self.kafelki[numer_2 - 1]["owner"] == '2':
                tekst_2 = f'\033[92m{numer_2:2d}\033[0m'
            else:
                tekst_2 = str(numer_2)
            top_bottom = f"+{'-'*(width+1)}+{' '*odleglosc_pomiedzy_kafelkami}+{'-'*(width+1)}+"
            middle = (
                f"|{' '*(width//2)}"
                f"{tekst}"
                f"{' '*(width//2)}|"
                f"{' '*odleglosc_pomiedzy_kafelkami}|"
                f"{' '*(width//2)}"
                f"{tekst_2}"
                f"{' '*(width//2)}|"
            )
            if i + 1 != height_of_board:
                wynik += top_bottom + "\n"
                wynik += middle + "\n"
                wynik += top_bottom + "\n"
            else:
                wynik += top_bottom + "\n"
                wynik += middle + "\n"
                wynik += top_bottom            
        return wynik

    def narysuj_gorny_lub_dolny_panel_planszy(self, czygornypanel):
        s = str(len(self.kafelki)).strip()
        width_of_board = len(self.kafelki) // 4 + 1
        height_of_board = len(self.kafelki) // 4 + 1
        top_bottom = ""
        middle = ""
        koncowka = 0
        width = len(s) + 3
        wynik = ""
        tekst = "25"
        for i in range(0, width_of_board):
            numer = len(self.kafelki) - width_of_board * 2 - i + height_of_board + 2
            numer_2 = 1 + i
            print(numer)
            if self.kafelki[numer - 1]["owner"] == '1':
                tekst = f'\033[96m{numer:2d}\033[0m'
            elif self.kafelki[numer - 1]["owner"] == '2':
                tekst = f'\033[92m{numer:2d}\033[0m'
            else:
                tekst = f"{numer:2d}"
                
            if self.kafelki[numer_2 - 1]["owner"] == '1':
                tekst_2 = f'\033[96m{numer_2:2d}\033[0m'
            elif self.kafelki[numer_2 - 1]["owner"] == '2':
                tekst_2 = f'\033[92m{numer_2:2d}\033[0m'
            else:
                tekst_2 = f"{numer_2:2d}"
            top_bottom += '+' + '-' * (width + 1) + '+ '
            if czygornypanel:
                middle += f'|{" " * (width // 2)}{tekst}{" " * (width // 2)}| '
            else:
                middle += f'|{" " * (width // 2)}{tekst_2}{" " * (width // 2 )}| '
            koncowka = i
            wynik = top_bottom + '\n'
            wynik += middle + '\n'
            wynik += top_bottom
        return wynik, koncowka