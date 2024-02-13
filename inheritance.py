class Person:
    def james(self):
        print("can talk")

    def tom(self):
        print("speaks english")

ll = Person()
print(ll.tom())
print(ll.james())


class Parrot(Person):
    def kilo(self):
        print("can sing")

tt = Parrot()

print(tt.james())
print(tt.kilo())
print(tt.tom())





