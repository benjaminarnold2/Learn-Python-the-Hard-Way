## Animal is a object - look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a object name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

##Person is-a object?
class Person(object):
    def __init__(self, name):
        ##Person has-a name
        self.name = name

        ## Person has-a pet
        self.pet = None

##Employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee has-a name and salary
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is-a cat
satan = Cat("Satan")

##mary is-a Person
mary = Person("Mary")

##Mary has-a pet that is satan
mary.pet = satan

##frank is-a Employee, frank has-a name of Frank, frank has-a salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet that is rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

##crouse is-a Salmon
crouse = Salmon()

##harry is-a Halibut
harry = Halibut()
