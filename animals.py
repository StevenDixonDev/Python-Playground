class Animal:
    def __init__(self, words) -> None:
        self.words = words
        pass
    
    def speak(self):
        print(self.words)


class Dog(Animal):
    pass

myDog = Dog('roof')

myDog.speak()
