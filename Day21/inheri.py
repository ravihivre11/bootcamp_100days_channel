class Dog:
    def __init__(self):
        self.temperament = "loyal"
 
class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.temperament = "gentle"

kittu = Dog()
print(kittu.temperament) 

robert = Labrador()
print(robert.temperament) 