# Programa per a que llegeixi tres nombres diferents i ens digui quin és el major.

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
