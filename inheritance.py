# """ parent class """
# class Animal:
#     livingthing=True
    
#     def eat():
#         print("eating")
        
#     def sleep():
#         print("sleep")

# # # # """child class"""
# class goat(Animal):
    
#     def grass():
#         print("Its eating grass")
        
#     def herb():
#         print("It is herbivorus")

#     def sleep():
#         print("Don't sleep you are 820Rs Kg")

# print(goat.livingthing)  # child class and accessing the parent class variable
# print(Animal.livingthing)  # parent class and accesing class variable
# goat.grass()
# # goat.herb()
# goat.eat()
# # goat.sleep()
# Animal.eat()
# Animal.sleep()
# Animal.herb()

""" Part-2 Calling with the help of an object"""
# class Animal:
#     livingthing=True
    
#     def eat(self):
#         print("eating")
        
#     def sleep(self):
#         print("sleep")

# """child class"""
# class goat(Animal):
    
#     def grass(self):
#         print("Its eating grass")
        
#     def herb(self):
#         print("It is herbivorus")

#     def sleep(self):
#         print("Don't sleep you are 710Rs Kg")

# a=Animal()
# print(a.livingthing)
# a.eat()
# a.sleep()

# g=goat()
# g.grass()
# g.herb()
# g.sleep()
# print(g.livingthing)
# g.eat()