import tkinter as tk
import os

PATH = "C:/Users/Mladen/Documents/Python/BEDcalc_GUI/"

root = tk.Tk()  # pocetak svakog
root.title("BED račun")

root.geometry("425x145")

canvas = tk.Canvas(root)  # dodavanje prozora na kojem se radi
canvas.pack()


def novi_prozor():
    window = tk.Toplevel(root)

    window.title("Konfiguracije")
    window.geometry("500x470")

    label = tk.Label(window, text="d = 2 Gy", font="Ubuntu 13 bold").place(x=100, y=15)
    label = tk.Label(window, text="d = 3 Gy", font="Ubuntu 13 bold").place(x=250, y=15)
    label = tk.Label(window, text="d = 4 Gy", font="Ubuntu 13 bold").place(x=400, y=15)
    label = tk.Label(window, text="BED", font="Ubuntu 15 bold", fg="red").place(
        x=10, y=11
    )

    ix = 10
    iy = 60
    for i in range(10):
        label_1 = tk.Label(
            window, text="n = " + str(i + 1), font="Ubuntu 13 bold"
        ).place(x=ix, y=iy)
        iy += 40

    d1 = 2
    dx = 120
    dy = 59
    for d in range(10):
        BED = round((d + 1) * d1 * (1 + (d1 / 10)), 2)
        label = tk.Label(window, text=str(BED), font="Ubuntu 12").place(x=dx, y=dy)
        dy += 40

    d2 = 3
    dxx = 270
    dyy = 59
    for d in range(10):
        BED = round((d + 1) * d2 * (1 + (d2 / 10)), 2)
        label = tk.Label(window, text=str(BED), font="Ubuntu 12").place(x=dxx, y=dyy)
        dyy += 40

    d3 = 4
    dxxx = 420
    dyyy = 59
    for d in range(10):
        BED = round((d + 1) * d3 * (1 + (d3 / 10)), 2)
        label = tk.Label(window, text=str(BED), font="Ubuntu 12").place(x=dxxx, y=dyyy)
        dyyy += 40
    root.mainloop()


############################################################################################################################
# prvi red
label1 = tk.Label(root, text="n1:", fg="blue").place(x=15, y=20)
broj_frakcija = tk.Entry(root, width=5)
broj_frakcija.place(x=40, y=20)

label1 = tk.Label(root, text="n2:", fg="red").place(x=80, y=20)
broj_frakcija2 = tk.Entry(root, width=5)
broj_frakcija2.place(x=105, y=20)
# drugi red
label2 = tk.Label(root, text="d1:", fg="blue").place(x=15, y=50)
doza_po_frakciji = tk.Entry(root, width=5)
doza_po_frakciji.place(x=40, y=50)

label2 = tk.Label(root, text="d1:", fg="red").place(x=80, y=50)
doza_po_frakciji2 = tk.Entry(root, width=5)
doza_po_frakciji2.place(x=105, y=50)
# treci red
label3 = tk.Label(root, text="\u03B1 / \u03B2:").place(x=38, y=80)
alpha_beta = tk.Entry(root, width=5)
alpha_beta.place(x=75, y=80)

# racun za BED
def BED_racun1():
    x1 = int(broj_frakcija.get())
    x2 = float(doza_po_frakciji.get())
    x3 = int(alpha_beta.get())
    BED1 = round(float(x1 * x2 * (1 + (x2 / x3))), 3)

    label5 = tk.Label(root, text=str(BED1) + " Gy!", font=30, fg="blue").place(
        x=240, y=28
    )


def BED_racun2():
    z1 = int(broj_frakcija2.get())
    z2 = float(doza_po_frakciji2.get())
    z3 = int(alpha_beta.get())
    BED2 = round(float(z1 * z2 * (1 + (z2 / z3))), 3)

    label5 = tk.Label(root, text=str(BED2) + " Gy!", font=30, fg="red").place(
        x=240, y=74
    )


def delta():
    x1 = int(broj_frakcija.get())
    x2 = float(doza_po_frakciji.get())
    x3 = int(alpha_beta.get())
    BED1 = round(float(x1 * x2 * (1 + (x2 / x3))), 3)
    z1 = int(broj_frakcija2.get())
    z2 = float(doza_po_frakciji2.get())
    z3 = int(alpha_beta.get())
    BED2 = round(float(z1 * z2 * (1 + (z2 / z3))), 3)
    razlika = round(BED1 - BED2, 2)
    label = tk.Label(root, text=str(razlika) + "Gy!", font="Ubuntu 12 bold").place(
        x=345, y=49
    )


def plus():
    x1 = int(broj_frakcija.get())
    x2 = float(doza_po_frakciji.get())
    x3 = int(alpha_beta.get())
    BED1 = round(float(x1 * x2 * (1 + (x2 / x3))), 3)

    z1 = int(broj_frakcija2.get())
    z2 = float(doza_po_frakciji2.get())
    z3 = int(alpha_beta.get())
    BED2 = round(float(z1 * z2 * (1 + (z2 / z3))), 3)

    zbir = round(BED1 + BED2, 2)

    label = tk.Label(root, text=str(zbir) + "Gy!", font="Ubuntu 12 bold").place(
        x=345, y=19
    )


def reset_window():
    root.destroy()
    os.startfile(PATH + "Kalkulacija_urednije.pyw")


def new_window():
    os.startfile(PATH + "Kalkulacija_urednije.pyw")


# dugme za novi prozor
nova_instanca = reset = tk.Button(
    root, text="Novi", height=1, width=4, fg="white", bg="green", command=new_window
)
reset.place(x=375, y=115)

# dugme za reset
reset = tk.Button(
    root, text="Reset", height=1, width=4, fg="white", bg="red", command=reset_window
)
reset.place(x=320, y=115)

# dugme za BED1
BED1 = tk.Button(root, text="BED1", height=2, width=8, fg="blue", command=BED_racun1)
BED1.place(x=160, y=20)
# dugme za BED2

BED2 = tk.Button(root, text="BED2", height=2, width=8, fg="red", command=BED_racun2)
BED2.place(x=160, y=65)

delta = tk.Button(root, text="\u0394", command=delta).place(x=320, y=50)
plus = tk.Button(root, text="+", command=plus).place(x=320, y=20)
Konfiguracije = tk.Button(
    root, text="Konfiguracije", height=1, width=12, command=novi_prozor
)
Konfiguracije.place(x=320, y=85)
############################################################################################################################
# sesti red
"""
label6 = tk.Label(root,text = "Dmax:").place(x=15,y=140)
Dmax=tk.Entry(root, width=5)
Dmax.place(x=110,y=140)

#sedmi red
label7 = tk.Label(root,text = "\u0394m").place(x=15,y=165)

broj_meseci=tk.Entry(root, width=5)
broj_meseci.place(x=110,y=165)

def Zaboravljeni_racun():
    y1=float(Dmax.get())
    y2=float(broj_meseci.get())
    zaborav = round(float((0.1/12)*y1*y2),3)

    label9 = tk.Label(root, text=str(zaborav) + ' Gy!', font=30, fg = "green").place(x=297,y=150)


#dugme za zaborav
zaborav = tk.Button(root, text="Zaboravljena doza", height = 3, width = 15, command = Zaboravljeni_racun)
zaborav.place(x=170,y=135)
"""
root.mainloop()  # kraj svakog
