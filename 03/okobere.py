from random import randrange


oko = 0
while True:
    pokracovat = input('Pokracovat? ')
    if pokracovat == 'Y':
        oko = oko + int(randrange(1, 12))
        print('OKO: ' + str(oko))
    else:
        break

print('KONEC HRY')
print('OKO:' + str(oko))

if oko < 21 or oko > 21:
    print('You LOST')
else:
    print('You WON')
