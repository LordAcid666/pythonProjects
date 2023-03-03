# https://www.youtube.com/playlist?list=PLFhH2Ohz-yTHAxYzLZB8kJ3V5RPqsiXnN

import tkinter as tk

# creiamo la finestra
window = tk.Tk()
window.title("la mia app")
window.geometry("900x500")
window.resizable(False, False)
window.config(bg="#232323")

# creaiamo i widget (scritte-bottoni-immagini)
label_ciao = tk.Label(window, text="ciao", font=("Times", 16), bg="#232323", fg="white")
label_ciao.grid(row = 1, column = 0, padx=350, pady=20)

# far partire la app 
window.mainloop()