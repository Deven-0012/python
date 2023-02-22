# class Animal:
#     def __init__(self):
#         print("animal created")
#
#     def who_am_i(self):
#         print("i am an animal")
#
#     def eat(self):
#         print("I am eating")
#
# myanimal = Animal()
#
# # print(myanimal.eat())
#
#
############ ------------->>>>>>>>..    this is called inheritance

# class Dog(Animal):
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog created")
#
#     def eat(self):
#         print("I am a eating dog")
#
#     def bark(self):
#         print("BHOWWWWW")
#
# mydog = Dog()
# print(mydog.bark())



############# ------------->>>>>>>>>..   Polymorphism


class Dog():
    def __init__(self,name):
        self.name = name

    def speak(self):
        return self.name + ' Bhowwww '


class Cat():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + ' MEOWWWW '

mydog = Dog("Tomy")
mycat = Cat("Cutie")
 # this print function just print the string's location where it is located         print(mydog)
print(mydog.speak())
print(mycat.speak())
