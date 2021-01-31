d1 = {
    10: "a",
    20: "b"
}

d2 = {
    30: "c"
}

print(f"d1: {type(d1)} = {d1}")
print(f"d2: {type(d2)} = {d2}")

d1i = d1.items()
d2i = d2.items()

print(f"d1i: {type(d1i)} = {d1i}")
print(f"d2i: {type(d2i)} = {d2i}")

d3 = dict(d1i)
d3.update(dict(d2i))
print(f"d3: {type(d3)} = {d3}")
