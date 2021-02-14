import random
import pyperclip as pc

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()=?*#'@"
passwords = []
Quit = False

while not Quit:
    promt = input("Was möchtest du tun? Schreibe neues Passwort, Passwörter anzeigen oder Beenden")
    if promt == "neues Passwort":
        number = input("Wie viele Passwörter möchtest du generieren?")
        number = int(number)

        length = input("Wie lang soll das Passwort jeweils sein? (12 Zeichen werden empfohlen)")
        length = int(length)
        if length < 8:
            print("Die meisten Websites benötigen 8 Zeichen.")
            continue

        for p in range(number):
            password = ""
            for c in range(length):
                password += random.choice(chars)
            if number == 1:
                print("Dein Passwort ist:", password, "Wir haben es für dich in die Passwortliste "
                                                      "hinzugefügt "
                                                      "und in die Zwischenablage gepackt.")
                pc.copy(password)
                passwords.append(password)

            else:
                print("Dein Passwort ist:", password, "Wir haben es für dich zur Passwortliste hinzugefügt.")
                passwords.append(password)
    elif promt == "Passwörter anzeigen":
        print(passwords)
        if len(passwords) == 0:
            print("Hier gibt es noch nichts zu sehen.")
    elif promt == "Beenden":
        warning = input("Willst du wirklich beenden? Alle deine generierten Passwörter gehen verloren.")
        if warning == "Ja" or "ja":
            Quit = True

    else:
        print("Hast du etwas falsch geschreiben? Oder nimmst du das hier nicht ganz ernst?")




