def paridispari():
     inp = input("Inserisci un numero: ")
     numero = int(inp)
     modulo = numero % 2
     if modulo == 0:
             print("numero pari")
     else:
             print("numero dispari")

paridispari()
