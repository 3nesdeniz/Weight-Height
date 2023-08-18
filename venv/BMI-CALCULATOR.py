import tkinter
from tkinter import *

window = Tk()
window.title("Boy-Kilo Endexi")
window.minsize(width=220, height=300)
sonuc = 0

def bmi_hesaplama():
    kilo = my_kilo.get()
    boy = my_boy.get()
    try:
        if boy == "" or kilo == "":
            Sonuc_label.config(text="Lütfen Parametreleri giriniz")
        else:
            sonuc = int(kilo) / ((int(boy) / 100) ** 2)
            if 1 < sonuc < 18.5:
                kategori = "İdeal Kilonun Altındasınız"
            elif 18.5 <= sonuc < 24.9:
                kategori = "İdeal Kilodasınız"
            elif 25 <= sonuc < 29.9:
                kategori = "Kilolu"
            elif 30 <= sonuc < 40:
                kategori = "Obez"
            else:
                kategori = "Aşırı Obez"
            Sonuc_label.config(text=f"Sonuç: {sonuc:.2f}\n{kategori}")
    except:
        Sonuc_label.config(text="Lütfen sadece sayı giriniz")

    Sonuc_label.pack()

my_label = tkinter.Label(text="Kilonuzu giriniz")
my_label.pack()
my_kilo = tkinter.Entry(width=20)
my_kilo.pack()

my_label_2 = tkinter.Label(text="Boyunuzu giriniz")
my_label_2.pack()
my_boy = tkinter.Entry(width=20)
my_boy.pack()

Sonuc_label = tkinter.Label()

button = tkinter.Button(text="Hesapla", command=bmi_hesaplama)
button.pack()

window.mainloop()