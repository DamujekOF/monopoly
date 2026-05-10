import math

class Plansza():
    def __init__(self, kafelki):
        self.kafelki = kafelki

    def narysuj_kolumny(self, koniec):
        s = str(len(self.kafelki))

        height_of_board = len(self.kafelki) // 4 - 1
        wynik = ""
        tekst = "26"
        for i in range(0, height_of_board):
            width = len(s) + ((height_of_board + 2)// 2) + 1
            width2 = width
            odleglosc_pomiedzy_kafelkami = (width + 4) * height_of_board + 1
            numer = len(self.kafelki) - height_of_board + i + 1
            numer_2 = koniec - i + height_of_board + 1
            display_gury = self.kafelki[numer - 1]["skrot"]
            display_dolu = self.kafelki[numer_2 - 1]["skrot"]
            dlugsc_tekstu_dolu = abs(width - len(display_dolu))
            dlugsc_tekstu_gury = abs(width - len(display_gury))

            top_bottom = f"+{'-'*(width+1)}+{' '*odleglosc_pomiedzy_kafelkami}+{'-'*(width+1)}+"
            if self.kafelki[numer - 1]["owner"] == 1:
                tekst = f'\033[96m{display_gury}\033[0m'
                width = dlugsc_tekstu_gury
            elif self.kafelki[numer - 1]["owner"] == 2:
                tekst = f'\033[92m{display_gury}\033[0m'
                width = dlugsc_tekstu_gury
            else:
                tekst = f"{display_gury}"
                width = dlugsc_tekstu_gury
            

            if self.kafelki[numer_2 - 1]["owner"] == 1:
                tekst_2 = f'\033[96m{display_dolu}\033[0m'
                width2 = dlugsc_tekstu_dolu
            elif self.kafelki[numer_2 - 1]["owner"] == 2:
                tekst_2 = f'\033[92m{display_dolu}\033[0m'
                width2 = dlugsc_tekstu_dolu
            else:
                tekst_2 = f"{display_dolu}"
                width2 = dlugsc_tekstu_dolu     


            middle = (
                f"|{' '*(math.ceil(width / 2))}"
                f"{tekst}"
                f"{' '*(math.ceil(width / 2))}|"
                f"{' '*odleglosc_pomiedzy_kafelkami}|"
                f"{' '*(math.ceil(width2 / 2))}"
                f"{tekst_2}"
                f"{' '*(math.ceil(width2 / 2))}|"
            )
            width = len(s) + ((height_of_board + 2)// 2) + 1
            wynik += "|" + " " * (width + 1) + "|" + ' ' * odleglosc_pomiedzy_kafelkami + "|" + " " * (width + 1) + "|" + "\n"
            wynik += middle + "\n"
            wynik += "|" + " " * (width + 1) + "|" + ' ' * odleglosc_pomiedzy_kafelkami+ "|" + " " * (width + 1) + "|" + "\n"        
            if i + 1 != height_of_board:
                wynik += top_bottom + "\n"
            else:
                wynik += top_bottom
        return wynik

    def narysuj_gorny_lub_dolny_panel_planszy(self, czygornypanel):
        s = str(len(self.kafelki)).strip()
        width_of_board = len(self.kafelki) // 4 + 1
        top_bottom = ""
        middle = ""
        width = len(s) + (width_of_board // 2) + 1
        koncowka = 0
        wynik = ""
        tekst = "25"
        for i in range(0, width_of_board):
            width = len(s) + (width_of_board // 2) + 1
            numer = len(self.kafelki) - width_of_board * 2 - i + width_of_board + 2
            numer_2 = 1 + i
            display_gury = self.kafelki[numer - 1]["skrot"]
            display_dolu = self.kafelki[numer_2 - 1]["skrot"]
            dlugsc_tekstu_dolu = abs(width - len(display_dolu))
            dlugsc_tekstu_gury = abs(width - len(display_gury))

        
            top_bottom += '+' + '-' * (width + 1) + '+ '

            if czygornypanel:
                if self.kafelki[numer - 1]["owner"] == 1:
                    tekst = f'\033[96m{display_gury}\033[0m'
                    width = dlugsc_tekstu_gury
                elif self.kafelki[numer - 1]["owner"] == 2:
                    tekst = f'\033[92m{display_gury}\033[0m'
                    width = dlugsc_tekstu_gury
                else:
                    tekst = f"{display_gury}"
                    width = dlugsc_tekstu_gury
            
            elif not czygornypanel:
                if self.kafelki[numer_2 - 1]["owner"] == 1:
                    tekst_2 = f'\033[96m{display_dolu}\033[0m'
                    width = dlugsc_tekstu_dolu
                elif self.kafelki[numer_2 - 1]["owner"] == 2:
                    tekst_2 = f'\033[92m{display_dolu}\033[0m'
                    width = dlugsc_tekstu_dolu
                else:
                    tekst_2 = f"{display_dolu}"
                    width = dlugsc_tekstu_dolu        
        
            if not czygornypanel:
                middle += f'|{" " * (math.ceil(width / 2))}{tekst_2}{" " * (math.ceil(width / 2))}| '
            else:
                middle += f'|{" " * (math.ceil(width / 2))}{tekst}{" " * (math.ceil(width / 2))}| '
            width = len(s) + (width_of_board // 2) + 1
            koncowka = i
            wynik = top_bottom + '\n'
            wynik += ("|" + " " * (width + 1) + "| ") * width_of_board + '\n'
            wynik += middle + '\n'
            wynik += ("|" + " " * (width + 1) + "| ") * width_of_board + '\n'
            wynik += top_bottom
        return wynik, koncowka
