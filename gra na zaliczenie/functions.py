from random import randint
import time
import sys

a = 0.2 #0.2
b = 0.1 #0.1

def SlowText(string, speed=0.05): #<-- 0.05
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)

class Shablon():
    def __init__(self, klasa, hp, mana) -> None:
        self.klasa = klasa
        self.hp = hp
        self.mana = mana

    def info(self):
        SlowText(f"Masz {self.hp} życia i {self.mana} many.\n", b)

    def bohater(self):
        SlowText(f"Grasz klasą {self.klasa}\n")

class Mob():
    def __init__(self, hp, nazwa) -> None:
        self.hp = hp
        self.nazwa = nazwa

def atak_bossa():
    boss_atak = randint(10, 20)
    atak_max = 20
    SlowText(f"{przeciwnik.nazwa} zaatakował!\n")
    gracz.hp -= boss_atak
    if boss_atak >= 4/5*atak_max:
        SlowText("\nCRITICAL HIT!\n\n")
    SlowText(f"{przeciwnik.nazwa} zadał/a ci {boss_atak} hp.\n")
    gracz.info()

def boss_fight():
    global przeciwnik
    przeciwnik = Mob(100, "Boss")

    SlowText("Jesteś w dość dużym pokoju...\n")
    SlowText(f"Walczysz teraz z Boss'em!\n")
    SlowText(f"{przeciwnik.nazwa} ma {przeciwnik.hp} hp!\n")
    while True:
        SlowText("atak zwykły - q, atak specjalny - e\n")
        while True:
            choice = input().lower()
            if choice == "q":
                atak_zwykly()
                break
            elif choice == "e":
                if gracz.mana <= 0:
                    SlowText("Nie możesz użyć tego ataku, masz za mało many.\n")
                    pass
                else:
                    atak_specjalny()
                    break
            else:
                SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
                pass
        if przeciwnik.hp > 0:
            atak_bossa()
            pass
        elif gracz.hp <= 0:
            SlowText("Przegrałeś!\n", a)
            quit()
        elif przeciwnik.hp <= 0:
            SlowText(f"Brawo! Zabiłeś Boss'a!!!\n", a)
            SlowText("Przeszedłeś grę...\n")
            SlowText("cdn...\n")
            break

def walka():
    global przeciwnik
    przeciwnik = rand_mob()
    SlowText(f"Napotkałeś na swojej drodze {przeciwnik.nazwa}!\n")
    mob_info()
    while True:
        SlowText("atak zwykły - q, atak specjalny - e\n")
        while True:
            choice = input().lower()
            if choice == "q":
                atak_zwykly()
                break
            elif choice == "e":
                if gracz.mana <= 0:
                    SlowText("Nie możesz użyć tego ataku, masz za mało many.\n")
                    pass
                else:
                    atak_specjalny()
                    break
            else:
                SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
                pass
        if przeciwnik.hp > 0:
            atak_przeciwnika()
            pass
        elif gracz.hp <= 0:
            SlowText("Przegrałeś!\n", a)
            quit()
        elif przeciwnik.hp <= 0:
            SlowText(f"Zabiłeś {przeciwnik.nazwa}!\n", a)
            break

def wybor():
    global gracz
    while True:
        choice = input().upper()
        if choice in ["Czlowiek", "Człowiek", "C"]:
            gracz = Shablon("Człowiek", 100, 50)
            gracz.info()
            break
        elif choice in ["Mag", "M"]:
            gracz = Shablon("Mag", 50, 100)
            gracz.info()
            break
        elif choice in ["Elf", "E"]:
            gracz = Shablon("Elf", 80, 70)
            gracz.info()
            break
        elif choice in ["Barb", "Barbarzyńca", "Barbarzynca", "B"]:
            gracz = Shablon("Barbarzyńca", 130, 20)
            gracz.info()
            break
        elif choice in ["Ork", "O"]:
            gracz = Shablon("Ork", 150, 0)
            gracz.info()
            break
        else:
            SlowText("Nie ma takiej klasy. Spróbuj ponownie.\n", b)
            pass

def atak_zwykly():
    obr = randint(5,15)
    SlowText(f"Zaatakowałeś! Zadałeś {obr} obrażeń!\n")
    przeciwnik.hp -= obr

def apteczka():
    SlowText("Zebrałeś apteczkę!\n")
    gracz.hp += 10
    gracz.info()
    return gracz.hp

def atak_specjalny():
    obr = randint(15,30)
    SlowText(f"Zaatakowałeś! Zadałeś {obr} obrażeń!\n")
    gracz.mana -= 10
    przeciwnik.hp -= obr
    gracz.info()

def potka():
    SlowText("Znalazłeś potkę! (dostajesz +10 many)\n")
    gracz.mana += 10
    gracz.info()
    return gracz.mana

def atak_przeciwnika():
    if przeciwnik.nazwa == "zombie":
        mob_atak = randint(1,5)
        atak_max = 5 
    elif przeciwnik.nazwa == "duch":
        mob_atak = randint(1,10)
        atak_max = 10
    elif przeciwnik.nazwa == "wiedźma":
        mob_atak = randint(1,15)
        atak_max = 15
    SlowText(f"{przeciwnik.nazwa} zaatakował/a!\n")
    gracz.hp -= mob_atak
    if mob_atak >= 4/5*atak_max:
        SlowText("\nCRITICAL HIT!\n\n")
    SlowText(f"{przeciwnik.nazwa} zadał/a ci {mob_atak} hp.\n")
    gracz.info()
        
# def zwracanie(zwrot, funkcje1, funkcje2, funkcje3):
#     if zwrot == "1":
#         wykonaj_po_kolei(funkcje1)
#     elif zwrot == "2":
#         wykonaj_po_kolei(funkcje2)
#     elif zwrot == "3":
#         wykonaj_po_kolei(funkcje3)

def zwracanie(zwrot, *args):
    count_empty = 0
    zwrot = int(zwrot)
    for arg in args:
        if arg == "":
            count_empty += 1
        elif count_empty == zwrot - 1:
            arg()

def tutorial():
    old_hp = gracz.hp
    old_mana = gracz.mana
    SlowText("Przechodzisz tutorial...\n")
    if trojga_drzwi() in ["2", "3"]:
        restart()
    prosto()
    walka()
    prawo()
    apteczka()
    lewo_prawo()
    gracz.hp = old_hp
    gracz.mana = old_mana
    SlowText("Brawo! przeszedłeś tutorial! (wszystkie statystyki zostały odnowione.)\n")

def wykonaj_po_kolei(funkcje):
    for funkcja in funkcje:
        funkcja()

def rand_mob():
    global przeciwnik
    rand = randint(1,3)
    if rand == 1:
        przeciwnik = Mob(15, "zombie")
        return przeciwnik
    elif rand == 2:
        przeciwnik = Mob(25, "duch")
        return przeciwnik
    elif rand == 3:
        przeciwnik = Mob(35, "wiedźma")
        return przeciwnik

def mob_info():
    SlowText(f"{przeciwnik.nazwa} ma {przeciwnik.hp} hp.\n")

def trojga_drzwi():
    global wybor
    SlowText("Trafiłeś do pokoju z trojgiem drzwi...\nWybierz mądrze... (1 lub 2 lub 3)\n")
    while True:
        wybor = input()
        if wybor == "1":
            SlowText("Wybrałeś drzwi o numerze 1...\n")
            return "1"
        elif wybor == "2":
            SlowText("Wybrałeś drzwi o numerze 2...\n")
            return "2"
        elif wybor == "3":
            SlowText("Wybrałeś drzwi o numerze 3...\n")
            return "3"
        else:
            SlowText("Nie ma drzwi o takim numerze...\n")
            pass
    
def dwoje_drzwi():
    SlowText("Trafiłeś do pokoju z dwojgiem drzwi...\nWybierz mądrze... (1 lub 2)\n")
    while True:
        choice = input()
        if choice == "1":
            SlowText("Wybrałeś drzwi o numerze 1...\n")
            return "1"
        elif choice == "2":
            SlowText("Wybrałeś drzwi o numerze 2...\n")
            return "2"
        else:
            SlowText("Nie ma drzwi o takim numerze...\n")
            pass

def restart():
    print("\nDokonałeś złego wyboru!\n")
    exit()

def prawo():
    SlowText("Możesz iść tylko w prawo (d)\n")
    while True:
        choice = input().lower()
        if choice == "d":
            SlowText("Poszedłeś prawym korytarzem...\n")
            return "2"
        else:
            SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
            pass

def lewo():
    SlowText("Możesz iść tylko w lewo (a)\n")
    while True:
        choice = input().lower()
        if choice == "a":
            SlowText("Poszedłeś lewym korytarzem...\n")
            return "1"
        else:
            SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
            pass

def prosto():
    SlowText("Możesz iść tylko prosto (w)\n")
    while True:
        choice = input().lower()
        if choice == "w":
            SlowText("Poszedłeś korytarzem na wprost...\n")
            return "3"
        else:
            SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
            pass

def lewo_prawo():
    SlowText("Możesz iść w lewo (a) lub w prawo (d)\n")
    while True:
        choice = input().lower()
        if choice == "a":
            SlowText("Poszedłeś lewym korytarzem...\n")
            return "1"
        elif choice == "d":
            SlowText("Poszedłeś prawym korytarzem...\n")
            return "2"
        else:
            SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
            pass

def lewo_prawo_prosto():
    SlowText("Możesz iść w lewo (a) lub w prawo (d) lub prosto (w)\n")
    while True:
        choice = input().lower()
        if choice == "a":
            SlowText("Poszedłeś lewym korytarzem...\n")
            return "1"
        elif choice == "d":
            SlowText("Poszedłeś prawym korytarzem...\n")
            return "2"
        elif choice == "w":
            SlowText("Poszedłeś korytarzem na wprost...\n")
            return "3"
        else:
            SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
            pass

def prawo_prosto():
    SlowText("Możesz iść w prawo (d) lub prosto (w)\n")
    while True:
        choice = input().lower()
        if choice == "d":
            SlowText("Poszedłeś prawym korytarzem...\n")
            return "2"
        elif choice == "w":
            SlowText("Poszedłeś korytarzem na wprost...\n")
            return "3"
        else:
            SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
            pass

def lewo_prosto():
    SlowText("Możesz iść w lewo (a) lub prosto (w)\n")
    while True:
        choice = input().lower()
        if choice == "a":
            SlowText("Poszedłeś lewym korytarzem...\n")
            return "1"
        elif choice == "w":
            SlowText("Poszedłeś korytarzem na wprost...\n")
            return "3"
        else:
            SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
            pass



