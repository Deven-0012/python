# class Sample():
#     pass
#
# my_sample = Sample
# type(my_sample)




# class Dog():
#     def __init__(self,breed):
#         self.breed = breed
#
# mydog = Dog(breed='Huskie')
# print(mydog.breed)



#
# class Dog():                       # this is called a class
#
#     species = 'mammal'
#     def __init__(self,breed,name,spots):
#         self.breed = breed        # this is called a attribbute
#         self.name = name
#         #expection a boolean true/false
#         self.spots = spots
#
#     def bark(self,number):                    # this is called a method
#         print('bhowwwww')
#         print('Bhowww my name is {} and number is {}'.format(self.name,number))
#
#
# mydog = Dog(breed='Huskie',name='Tommy',spots=False)
# print(mydog.breed)
# print(mydog.name)
# print(mydog.spots)
# print(mydog.species)
# print(mydog.bark(3))








class Circle():
 # class oobject attritbute
    pie = 3.14
# Default init function
    def __init__(self,radius=1):
        self.radius = radius
        self.area = radius * radius * self.pie # we could also write radius * radius * Circle.pie because it is class object  attribute
# Method
    def get_circumference(self):
        return self.radius * self.pie *2


my_circle = Circle(8)
print(my_circle.radius)
print(my_circle.get_circumference())
print(my_circle.area)







