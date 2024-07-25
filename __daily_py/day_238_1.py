class Food:
    def __init__(self):
        self.taste = 'salty'

class Chocolate(Food):
    def __init__(self):
        self.taste = 'sweet'

class Pasta(Food):
    pass 

if __name__ == "__main__":
    choc = Chocolate()
    pasta = Food()
    print(choc.taste, pasta.taste)