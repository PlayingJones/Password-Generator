import tkinter as tk
import random
import pyperclip as pc

root = tk.Tk()
root.resizable(False, False)
root.title("   ")

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# Header
Header = tk.StringVar()
text = tk.Label(root, textvar=Header, font="helvetica")
Header.set("Passwort Generator")

chars = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!§$%&/()=?*#'@"
passwords = []

text.place(x=238, y=10)


def passwort_gen():
    Header.set("Neues Passwort")
    password = ""
    for p in range(1):
        password = ""
        for c in range(12):
            password += random.choice(chars)
    pwtext = tk.StringVar()
    showpw = tk.Label(root, textvar=pwtext, font="helvetica", fg="#000000")
    pwtext.set("Dein Passwort ist:" + password + ". Es wurde zum Clipboard hinzugefügt")
    showpw.place(x=85, y=250)
    showpw.after(10000, showpw.destroy)
    pc.copy(password)
    passwords.append(password)


def passwort_show():
    Header.set("Passwörter anzeigen")
    if 1 <= len(passwords) <= 4:
        liste = tk.StringVar()
        showliste = tk.Label(root, textvar=liste, font="helvetica")
        liste.set(passwords)
        showliste.place(x=85, y=250)
        showliste.after(10000, showliste.destroy)
    elif len(passwords) > 4:
        warning2 = tk.StringVar()
        warning2show = tk.Label(root, textvar=warning2, font="helvetica")
        warning2.set("Mehr als 4 Passwörter können nicht angezeigt werden.")
        warning2show.place(x=85, y=250)
        warning2show.after(5000,  warning2show.destroy)
    else:
        warning = tk.StringVar()
        showwarning = tk.Label(root, textvar=warning, font="helvetica")
        warning.set("Du hast noch keine Passwörter generiert.")
        showwarning.place(x=85, y=250)
        showwarning.after(10000, showwarning.destroy)


def back():
    Header.set("Passwort Generator")


# button
text = tk.StringVar()
browse_btn = tk.Button(root, textvar=text, command=lambda: passwort_gen(), font="helvetica")
text.set("neues Passwort")
browse_btn.place(x=245, y=125)

# button2
text2 = tk.StringVar()
list_btn = tk.Button(root, textvar=text2, command=lambda: passwort_show(), font="helvetica")
text2.set("Passwörter anzeigen")
list_btn.place(x=230, y=155)

# button3
text3 = tk.StringVar()
back_btn = tk.Button(root, textvar=text3, command=lambda: back(), font="helvetica")
text3.set("Zurück")
back_btn.place(x=266, y=185)

root.mainloop()
