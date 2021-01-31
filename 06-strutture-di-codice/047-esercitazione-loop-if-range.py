"""
CREARE UNA LISTA CHE CONTENGA:
    - I NUMERI PARI TRA  10 E 25
    - USANDO UN FOR LOOP TRA 10 E 30
"""

pariTra10E25 = list()               # creo lista vuota

for pari in range(10, 30, 2):       # ciclo tra i numeri pari compresi tra 10 e 30
    if pari < 25:                   # se il numero e' inferiore a 25
        pariTra10E25.append(pari)   # aggiungo alla lista

print(pariTra10E25)
