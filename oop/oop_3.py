
"""
    Challenge: Model a Farm
    1. We should have at least four classes: the parent Animal class, and then at least three child animal classes that inherit from Animal. 
    2. Each class should have a few attributes and at least one method that models some behaviour appropriate for a specific animal or all animals. 
    3. Keep it simple. Utilize inheritance. 
"""

class Animals:
    
    def __init__(self, species, move):
        self.species = species
        self.move = move 

    def __str__(self):
        return f"{self.species} {self.move} in jungle."

    def eat(self, food):
        return f"{self.species} is eat {food}"

class Mammal(Animals):
    pass

class Fly(Animals):
    pass 

class Insect(Animals):
    pass

elephant = Mammal("Elephant", "walk")
print(elephant)

bird = Fly("Saka", "flying")
print(bird)

ant = Insect("Ant", "crawling")
print(ant)

print(elephant.eat("leaf"))
print(bird.eat("insect"))