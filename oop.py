# # object-oriented programming
# class Fruits:
#     def __init__(self):
#         self.name = "apple"
#         self.color = "red"
#
#
# fruits = Fruits()
# fruits.color = "green"
# fruits.name = "mango"
#
# print(fruits.name)
#
# print(fruits.color)



class Fruits:
    def __init__(self, name, color):
        self.name = name
        self.color = color


fruit1 = Fruits("apple", "red")
fruit2 = Fruits("mango", "yellow")
fruit3 = Fruits("watermelon", "green")
fruit4 = Fruits("banana", "green")
fruit5 = Fruits("pawpaw", "green")

print(fruit4.name)
print(fruit1.color)

print(f"The name of the fruit: {fruit3.name}")
print(f"The color of the fruit: {fruit3.color}")
print(f"The name of the first fruit: {fruit1.name}")
print(f"The color of the first fruit : {fruit1.color}")
print(f"The name of the second fruit : {fruit2.name} ")
print(f"The color of the second fruit :{fruit2.color}")



