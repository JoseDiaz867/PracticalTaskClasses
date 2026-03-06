import random

class Human:
    def __init__(self, name : str):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"
    
    @classmethod
    def species(cls):
        return "You are a species of homo sapiens"

    @staticmethod
    def arbitrary_message():
        return f"Your lucky number of today is {random.randint(1, 50)}."
    
# Test.

person1 = Human("Pepe")
print(person1.welcome())
print(Human.species())
print(Human.arbitrary_message())