# Progrma per a indentificar si ets o no major d'edat.

# Pregunta sobre l'edat
edat = input("Quina és la teva edat?:")

edat = int(edat)

# Si l'edat que ens posa la persona és més gran o igual que 18, llavos és major.

if 18 <= edat:
    print ("Bé, ets major")

# Si no, llavors vol dir que és menor.
elif 18 > edat:
    print ("Mal, ets menor")
