# IMPORT
import random
from time import sleep

# VARIAVLES GENERALS
#opcio = 0

# FUNCIONS
def Area_cuadrat():
    # L'usuari ha d'introduir l'unitat
    costat = float(input("Itrodueix la mida del costat del quadrat: "))
    # Càlcul
    area = costat * costat
    # Resultat final de l'area del quadrat
    print ("L'àrea del quadrat és", area)

def Calcul_dos_nombre():
    # Introducció dels dos numeros
    Num1 = float(input("Introdueix el primer nùmero: "))
    Num2 = float(input("Introdueix el segon nùmero: "))
    # Dona el resultat de la suma
    print ("La súma és", Num1 + Num2)
    # Dona el resultat de la resta 
    print ("La resta és", Num1 - Num2)
    # Dona el resultat de la multiplicació
    print ("La multiplicació és", Num1 * Num2)
    # Dona el resultat de la divisió
    print ("La divisió és", Num1 / Num2)

def Fer_frase():
    # Primera paraula per a la frase
    paraula1 = input("Escriu la primera paraula: ")
    # Segona paraula per a la frase
    paraula2 = input("Escriu la segona paraula: ")
    # Tercera paraula per a la frase
    paraula3 = input("Escriu la tercera paraula: ")
    print("La frase és: ", paraula1, paraula2, paraula3 )

def Numeros_flotants():
    # Dos nombres en coma flotant retornin un valor enter
    num1 = float(input("Introdueix el primer valor: "))
    num2 = float(input("Intdodueix el segon valor: "))
    # Operació
    suma = num1 + num2
    # Cambiar a resultat enter
    valor_enter = int(suma)
    # Resultat final
    print("El resultat de la operació és:", valor_enter)

def Comprovació_edat ():
    # Pregunta sobre l'edat
    edat = input("Quina és la teva edat?:")
    edat = int(edat)
    # Si l'edat que ens posa la persona és més gran o igual que 18, llavos és major.
    if 18 <= edat:
        print ("Bé, ets major")
    # Si no, llavors vol dir que és menor.
    elif 18 > edat:
        print ("Mal, ets menor")

def Nombre_major_menor():
    nombre1 = float(input("Primer nombre: "))
    nombre2 = float(input("Segon nombre: "))
    nombre3 = float(input("Tercer nombre: "))
    # Si el nombre1 és més gran o igual que el nombre2 i si és més gran o igual que el nombre3, llavors ell ha de ser el major.
    if nombre1 >= nombre2 and nombre1 >= nombre3:
        print(nombre1, "és el major")
    # Si el nombre2 és més gran o igual que el nombre1 i si és més gran o igual que el nombre3, llavors ell ha de ser el major.
    elif nombre2 >= nombre1 and nombre2 >= nombre3:
        print(nombre2, "és el major")
    # Si el resultat no és cap del anterior, llavors ell ha de ser el major.
    else: 
        print(nombre3, "és el major")

def Nombre_negatiu_positiu ():
    nombre = float(input("Dis-me un nombre: "))
    # Si el nombre és més gran que 0 ens dira que és positiu.
    if nombre >= 0:
        print ("Aquest nombre és positiu.")
    # Si el nombre és més menor que 0 ens dira que és negatiu.
    elif nombre < 0:
        print("Aquest nombre és negatiu.")

def Nombres_parells():
    numero = 0
    # Estem dien que quan el valor de numero estigui entre 1 i 201 ens mostri tots el numeros.
    for numero in range (numero ,201 , 2):
        print (numero)

def Notes_0_10():
    notes = 0
    deus = 0
    while notes != -1:
        notes = int(input("Escriu una nota entre 0 i 10: "))
        if notes == 10:
            deus = 1
    if deus == 1:
        print("Hi ha hagut un 10")

def Bucle_10_negatius():
    negatiu = 0
    for i in range (10):
        negatiu = int(input("Escriu un numero: "))
        if negatiu < 0:
            negatiu == 1 
    if negatiu == 1:
        print ("Hi ha un nombre negatiu")
    else:
        print ("No hi ha cap nombre negatiu")



# MAIN
if __name__ == "__main__":
    while True:
        print ("1: Area_cuadrat")
        print ("2: Calcul_dos_nombres")
        print ("3: Fer_frase")
        print ("4: Numeros_flotants")
        print ("5: Comprovació_edat")
        print ("6: Nombre_major_menor")
        print ("7: Nombre_negatiu_positiu")
        print ("8: Nombres_parells")
        print ("9: Notes_0_10")
        print ("10: Bucle_10_negatius")
        print ("SORTIR: S")

        opcio = input("Tria una opció del 1 al 10: ")
        
        opcio = opcio.upper()

        match  opcio:
            case "1":
                Area_cuadrat()
            case "2":
                Calcul_dos_nombre()
            case "3":
                Fer_frase()
            case "4":
                Numeros_flotants()
            case "5":
                Comprovació_edat()
            case "6":
                Nombre_major_menor()
            case "7":
                Nombre_negatiu_positiu()
            case "8":
                Nombres_parells()
            case "9":
                Notes_0_10()
            case "10": 
                Bucle_10_negatius()
            case "S":
                print ("Gràcies per la participació!")
                break
            case _:
                print("Opció incorrecta")
        sleep(2)






