from functions import *
# a = 0.2
# b = 0.1
a = 0.2
b = 0.1

SlowText("Witaj w grze! Wybierz klasę swojego bohatera:\nKlasy do wyboru: ", b)
SlowText("\nCzłowiek\nMag\nElf\nOrk\nBarbarzyńca\n", b)
SlowText("Wybierz klasę podróżniku:\n", a)
wybor()

SlowText("Czy chcesz przejść tutorial? (t/n)\n", a)
while True:
    tut = input().lower()
    if tut in ['tak', 't']:
            tutorial()
            break
    elif tut in ['nie', 'n']:
        break
    else:
        SlowText("Niepoprawny wybór. Spróbuj ponownie.\n")
        pass

i = 0

SlowText("Naciśnij [p] aby zacząć rozgrywkę...\n",a)

while i < i+1:

    c = input().lower()
    if c == "p":
        break
    else:
        if i == 0:
            text = "Niepoprawny wybór. Spróbuj ponownie.\n"
            d = 0.05
        elif i == 1:
            text = "Masz wyraźnie napisane: Naciśnij [p] aby zacząć rozgrywkę...\n"
            d = 0.05
        elif i == 2:
            text = "No naciśnij [p] debilu\n"
            d = 0.05
        elif i == 3:
            text = "...\n"
            i -= 1
            d = 0.3
        SlowText(text, d)
        i+=1
        

SlowText("Jesteś na starcie...\n")

# ---------------------------------- lewa strona -------------------------------

def dalsza_czesc_kodu():
    zwracanie(lewo_prawo(), prosto, apteczka, prosto, walka, apteczka, potka, prosto, boss_fight, "", prosto, walka, prosto, dalsza_czesc_kodu2_8) 

def dalsza_czesc_kodu2():
    zwracanie(prawo_prosto(), "", dalsza_czesc_kodu2_2, "", dalsza_czesc_kodu2_3)

def dalsza_czesc_kodu2_3():
    zwracanie(prawo_prosto(), "", dalsza_czesc_kodu2_4, "", dalsza_czesc_kodu2_7)

def dalsza_czesc_kodu2_4():
    zwracanie(dwoje_drzwi(), prosto, dalsza_czesc_kodu2_5, "", restart)

def dalsza_czesc_kodu2_5():
    zwracanie(lewo_prawo(), prosto, dalsza_czesc_kodu2_6, "", prosto, walka, prawo, apteczka, potka, prosto, boss_fight)

def dalsza_czesc_kodu2_6():
    zwracanie(lewo_prosto(), prosto, prawo, walka, prosto, prawo, walka, prosto, apteczka, potka, boss_fight,  "", "", apteczka, prawo, apteczka, potka, prosto, boss_fight)

def dalsza_czesc_kodu2_7():
    zwracanie(lewo_prawo(), prosto, walka, prosto, prawo, walka, prosto, apteczka, potka, prosto, boss_fight, "", prosto, apteczka, prawo, apteczka, potka, prosto, boss_fight)

def dalsza_czesc_kodu2_8():
    zwracanie(trojga_drzwi(), prosto, potka, dalsza_czesc_kodu2_9, "", restart, "", prosto, walka, prosto, apteczka, potka, prosto, boss_fight)

def dalsza_czesc_kodu2_9():
    zwracanie(lewo_prosto(), walka, prosto, potka, apteczka, prosto, boss_fight, "", "", prosto, apteczka, potka, prosto, boss_fight)

def dalsza_czesc_kodu2_2():
    zwracanie(dwoje_drzwi(), restart, "", prosto, potka, lewo, potka, apteczka, boss_fight)

def lewa_strona():
    zwracanie(dwoje_drzwi(), prosto, "",  restart)
    zwracanie(lewo_prawo(), prosto, potka, prosto, dalsza_czesc_kodu, "", prosto, walka, dalsza_czesc_kodu2)

# ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !
    
lewa_strona()

# ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! !

#-------------------------------------------------------------------------------