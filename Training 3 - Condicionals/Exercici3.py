# Programa que llegeixi per teclat un nombre i ens digui si és positiu o negatiu (considerem el zero com a positiu).

nombre = float(input("Dis-me un nombre: "))

# Si el nombre és més gran que 0 ens dira que és positiu.
if nombre >= 0:
    
    print ("Aquest nombre és positiu.")

# Si el nombre és més menor que 0 ens dira que és negatiu.
elif nombre < 0:

    print("Aquest nombre és negatiu.")
