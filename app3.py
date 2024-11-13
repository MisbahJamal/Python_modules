square=lambda x: x**2
print(square(7))


#oranother example 

f=lambda num: num*num
result=f(8)
print(result)


# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name
#         self.breed = breed
#         self.age = age

#     def bark(self):
#         print("Woof")

# my_dog = Dog('pet', 'German Shepherd', 3)
# my_dog.bark()


#####class####
class Car:
    def __init__(self, model, name):
        self.model = model
        self.name = name

    def func(self):
        return self.model + " is a car from " + str(self.name)

class ElectricCar(Car):
    def __init__(self, model, name, battery_capacity):
        super().__init__(model, name)
        self.battery_capacity = battery_capacity

my_e_class = ElectricCar('2024', 'Tesla', '2000km/h')
print(my_e_class.func())

my_class = Car('2004', 'Mercedez')
print(my_class.model)
print(my_class.name)
print(my_class.func())



class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

my_account = BankAccount(1000)
my_account.deposit(500)
print(my_account.get_balance()) 




class Animal:
    def sound(self):
        print("The animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

class Cat(Animal):
    def sound(self):
        print("The cat meows.")

def make_sound(animal):
    animal.sound()

my_dog = Dog()
my_cat = Cat()

make_sound(my_dog) 