import random

print("Willkommen bei dem Spiel Zahlen raten!")
print("Gesucht ist eine Zahl zwieschen 1 und 100 und "
      "du hast 7 Versuche.")
print("Viel Spass.")
zufallzahl = random.randint(1, 100)
versuche = 7

while versuche > 0:
    versuche -= 1
    print("Deine Schätzung:")
    inpt = input()
    a = int(inpt)
    if zufallzahl > a:
        print("Die gesuchte Zahl ist grösser")
    if zufallzahl < a:
        print("Die gesuchte Zahl ist kleiner")
    elif zufallzahl == a:
        print("Du hast die gesuchte Zahl gefunden")
        print("Du hättest noch " + str(versuche) + "Versuche übrig")
        break
    print("Du hast noch " + str(versuche) + "Versuche übrig")
    if versuche == 0:
        print("Du hast leider verloren! Versuche es noch ein mal!")
