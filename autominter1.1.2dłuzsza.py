
#WERSJA WOLNA SKUTECZNA UPGRADE v.1.0.2 do 1.1.2

import pyautogui
import time

# Funkcja do wykonania akcji w określonym punkcie
def perform_action(x, y):
    pyautogui.moveTo(x, y)
    time.sleep(2)
    pyautogui.click(button='left')
    time.sleep(5)

# Pobranie liczby pętli od użytkownika
num_loops = int(input("Podaj liczbę pętli: "))
n = 1
perform_action(1340, 242)

for _ in range(num_loops):
    print(n, ' z ', num_loops)
    # Jedź do miejsca: STOP MINT XENFT
    
    
    perform_action(1340, 240)

    # Jedź do miejsca: STOP czarny MINT
    perform_action(716, 624)

    #perform_action(711, 590)

    # Jedź do miejsca: STOP okienko mm
    perform_action(1251, 377)

    # Jedź do miejsca: STOP scroll
    pyautogui.click(button='left')
    time.sleep(1)
    pyautogui.scroll(-1)
    time.sleep(1)
    pyautogui.scroll(-1)
    time.sleep(1)
    pyautogui.scroll(-2)
    time.sleep(5)

    # Jedź do miejsca: STOP potwierdz
    perform_action(1351, 609)
    pyautogui.click(button='left') #dodano

    # Jedź do miejsca: STOP wyjscie i czekanie 40s
    perform_action(998, 767)
    time.sleep(90)
    n += 1 
