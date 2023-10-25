class Animal:
    color = "white"

    def __init__(self, nickname, weight ) -> None:
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

class Dog(Animal):

    def __init__(self, nickname, weight, breed) -> None:
        super().__init__(nickname, weight)
        self.breed = breed

    def say(self):
        return "Woof"
    
dog = Dog("Barbos", 23, "labrador")
print(dog.say())
print(dog.breed)