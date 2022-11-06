from faker import Faker
from tkinter import *
import csv
import time

with open('database.csv', 'r', encoding='UTF-8') as database:
    dane = []
    _reader = csv.reader(database)
    for row in _reader:
        if not row:
            continue
        dane.append(row)

lista = []

for pom in dane[1:]:
    lista.append(pom[1])

root = Tk()
root.geometry("300x200")
clicked = StringVar()
drop = OptionMenu(root, clicked, *lista)
drop.grid(row=0, column=0)

karnet = ""
x = 0

def load():
    global x, karnet
    x = lista.index(clicked.get()) +1
    karnet = dane[x][2]
    czas = dane[x][3]
    label1.config(text=czas)

    if karnet == "False":
        guzik2.config(text='Enter')

    else:
        guzik2.config(text='Exit')

    guzik2.grid(row=1, column=1)

def gate(): # pisane gdy rudy grał w bedwarsy i przegrał XD
    global x
    if dane[x][2] == "False":
        dane[x][2] = "True"
        guzik2.config(text='Exit')

        dane[x][4] = round(time.time() / 60)

    else:
        dane[x][2] = "False"
        guzik2.config(text='Enter')

        k = int(dane[x][3])
        k -= round(time.time() / 60) - int(dane[x][4])
        dane[x][3] = k
        czas = dane[x][3]
        label1.config(text=czas)
        dane[x][4] = 0

    with open('database.csv', 'w', encoding="utf-8") as database:
        writer_varible = csv.writer(database)
        writer_varible.writerows(dane)



guzik = Button(root, text='confirm', command=load)
guzik.grid(row=0, column=1)

label1 = Label(root, text = " ")
label1.grid(row=1, column=0)

guzik2 = Button(root, text=' ', command=gate)






root.mainloop()
