# Escriu un programa que llegeixi 10 nombres.
# Quan acabi ha d'indicar si "hi havia almenys un nombre negatiu" o "no hi ha cap nombre negatiu".

negatiu = 0

for i in range (10):
    negatiu = int(input("Escriu un numero: "))

    if negatiu < 0:
        negatiu == 1 

if negatiu == 1:
    print ("Hi ha un nombre negatiu")
else:
    print ("No hi ha cap nombre negatiu")
    