#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    pass
    def __init__(self, name = None, breed = None):
        self._name = None
        self._breed = None  

        if name is not None:
            self.name = name  

        if breed is not None:
            self.breed = breed    

    def get_name(self):
        print('Retrieving name...')
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")  

    def get_breed(self):
        print('Retrieving breed...')
        return self._breed

    def set_breed(self, breed):
        if(breed in APPROVED_BREEDS):
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds.")    


    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)

my_dog = Dog()

my_dog.name = 'test'
my_dog.breed = 'fsbvjhj'

print('Pug' in APPROVED_BREEDS)





