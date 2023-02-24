from random import random


#1 leggi il tentativo dell'utente
tentativo = input("Cosa esce T/C: ")
tentativo = tentativo.strip().upper()

#2 simula il lancio della moneta
caso = random()

if caso < 0.5:
    moneta = 'T'
else:
    moneta = 'C'

#3 determina se l'utente ha vinto

print("Tentativo =", tentativo, "- Moneta =", moneta)

if tentativo == moneta:
    print("VINTO")
else:
    print("PERSO")
