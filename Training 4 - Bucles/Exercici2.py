# Programa que llegeixi una seqüència de notes (valors de 0 a 10) i finalitzarà la seqüència amb el valor -1.
# Quan finalitzi ens ha d'indicar si "Hi ha hagut alguna nota que té un 10" o "No hi ha cap 10".

notes = 0
deus = 0

while notes != -1:
    notes = int(input("Escriu una nota entre 0 i 10: "))

    if notes == 10:
        deus = 1
if deus == 1:
    print("Hi ha hagut un 10")
 
