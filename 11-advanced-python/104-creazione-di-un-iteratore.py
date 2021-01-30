class MyIterator:
    def __iter__(self):
        self.myattr = 2
        return self

    def __next__(self):
        if self.myattr < 300:
            n = self.myattr
            self.myattr *= 2
            return n
        else:
            print("StopIteration")
            raise StopIteration


myiterator = MyIterator()
print(myiterator)
print(type(myiterator))
# print(next(myiterator))   // AttributeError: 'MyIterator' object has no attribute 'myattr'

it1 = iter(myiterator)
print(it1)
try:
    print(type(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))
    print(next(it1))        # StopIteration
    # exit()
except StopIteration as si:
    pass

print("\nfor i in iter(MyIterator()):")
for i in iter(MyIterator()):
    print(i)

print("\nfor i in MyIterator():")
for i in MyIterator():
    print(i)