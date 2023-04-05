#!/usr/bin/env python3
import ipdb 

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
    #Set what happens in initial state
    def __init__(self,name = "Fido", breed = "Mastiff"):
        self.name = name
        self.breed = breed
        
    #Defining Name Property  
    def get_name(self):
        return self._name
    
    def set_name(self,name):
        if (type(name) == str) and (0<len(name)<=25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
        
    name = property(get_name,set_name,)
    
    # Define Breed Property:
    def get_breed (self):
        print("Retrieving Breed...")
        return self._breed
    
    def set_breed (self, breed):
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            print("Breed must be in list of approved breeds.")
    
    breed = property(get_breed, set_breed,)
    
    
# ipdb.set_trace()



