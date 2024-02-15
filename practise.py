
class people:
    def dan(self):
        print("likes to speak")

    def cliff(self):
        print("likes to dance")

hh = people()
print(hh.dan())
print(hh.cliff())

class animal(people):
    def lion(self):
        print("can roar")




    def zebra(self):
        print("can run")

yy = animal()
print(yy.zebra())
print(yy.lion())
print(yy.cliff())
print(yy.dan())



def python(a, b):
    return a+b
