

# a = 356 #tohle je komentar

strana = float(input('Zadej cislo: '))

correct = strana >= 0

if correct:
    print("Obvod ctverce se stranou ", strana, " je: ", 4 * strana, " cm")
else:
    print("Chod do rite!")

print("Konec programu")
