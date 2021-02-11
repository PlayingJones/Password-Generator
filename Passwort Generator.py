from tkinter import Tk
import random
chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()=?*#'@"
passwords = []
Quit = False

while not Quit:
    promt = input("Was möchtest du tun? Schreibe neues Passwort, Passwörter anzeigen, oder Beenden")
    if promt == "neues Passwort":
        number = input("Wie viele Passwörter möchtest du generieren?")
        number = int(number)

        length = input("Wie lang soll das Passwort sein? (12 Zeichen werden empfohlen)")
        length = int(length)
        if length < 8:
            print("Die meisten Websites benötigen 8 Zeichen.")
            continue

        for p in range(number):
            password = ""
            for c in range(length):
                password += random.choice(chars)
            print("Dein Passwort ist:", password, "Wir haben es für dich in die Passwortliste "
                                                  "hinzugefügt "
                                                  "und in die Zwischenablage gepackt.")
            passwords.append(password)
            r = Tk()#needs to be fixed/replaced
            r.withdraw()
            r.clipboard_clear()
            r.clipboard_append(password)
            r.update()
            r.destroy()
    elif promt == "Passwörter anzeigen":
        print(passwords)
        if len(passwords) == 0:
            print("Hier gibt es noch nichts zu sehen.")
    elif promt == "Beenden":
        warning = input("Willst du wirklich beenden? Alle deine Passwörter gehen verloren.")
        if warning == "Ja":
            Quit = True

    else:
        print("Du nimmst das hier wohl nicht ganz ernst!?")




