# https://www.youtube.com/playlist?list=PLFhH2Ohz-yTHAxYzLZB8kJ3V5RPqsiXnN

import tkinter as tk
from tkinter.font import BOLD, ITALIC

# creiamo la finestra
window = tk.Tk()
window.title("la mia app")
window.geometry("900x500")
window.resizable(False, False)
window.config(bg="#232323")

# creaiamo i widget (scritte-bottoni-immagini)
label_ciao = tk.Label(window, text="ciao", font=("Times", 16, BOLD), bg="#232323", fg="white")
label_ciao.grid(row = 1, column = 0, padx=350, pady=20)

label_indicazione = tk.Label(window, text="Clikka il bottone qui sotto:", font=("Times", 16, ITALIC), bg="#232323", fg="white")
label_indicazione.grid(row = 2, column = 0, padx=350, pady=20)

bottone_cliccami = tk.Button(window, text="cliccami", bd = 5, width=20)
bottone_cliccami.grid(row = 3, column = 0, padx=350, pady=20)


# far partire la app 
window.mainloop()