piano = int(input("Piano?: "))


if piano <= 12:
    piano_vero = piano
    print("piano basso")
else:
    piano_vero = piano - 1
    print("piano alto")


print("vuoi andare al piano: ", piano)
print("andiamo al piano VERO: ", piano_vero)


