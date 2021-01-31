def get_doppio_gen():
    e = 2
    # while e < 300:
    while True:
        yield e
        e *= 2
        if e >= 300:
            return      # StopIteration

print(type(get_doppio_gen))

gen = get_doppio_gen()
print(type(gen))
print(gen)

print(next(gen))        # 2
print(gen.__next__())   # 4
print(next(gen))        # 8
print(next(gen))        # 16
print(next(gen))        # 32
print(next(gen))        # 64
print(next(gen))        # 128
print(next(gen))        # 256

