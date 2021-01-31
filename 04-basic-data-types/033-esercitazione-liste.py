mylist = [1, 2, 3, 4, 5]

primidue = mylist[:2]
print(primidue)

secondoeterzo = mylist[1:3]
print(secondoeterzo)

"""
INSERISCI 6 COME ELEMENTO ALLA POSIZIONE 2 DELLA LISTA (SECONDA SAREBBE PIU' CORRETTO,
SENZA SOSTITUIRE GLI ELEMENTI GIA' PRESENTI
"""
mylist.insert(1, 6)
print(mylist)

"""
AGGIUNGI IN CODA IL VALORE 10
"""
mylist.append(10)
print(mylist)

"""
ELIMINA IL VALORE ALLA QUARTA POSIZIONE
"""
del mylist[4]
print(mylist)
