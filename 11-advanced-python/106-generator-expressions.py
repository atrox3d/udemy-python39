oddgen = (n * n for n in range(1, 10) if n % 2 == 1)
print(type(oddgen))

for e in oddgen:
    print(e)

for e in oddgen:    # generatore esaurito, nessun output
    print(e)
