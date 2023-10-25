class Animal:

    def __init__(self, nickname, weight ) -> None:
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

class Owner:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address        

    def info(self):
        return vars(owner)       


class Dog(Animal):
    def __init__(self, nickname, weight, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(nickname, weight)

    def say(self):
        return "Woof"

    def who_is_owner(self):
        return Owner.info(self)
    
owner = Owner("Anatolii", 38, "Kharkiv, Dragomanova 8")
dog = Dog("Barbos", 23, "labrador", owner)
print(owner.name)
print(dog.breed)
print(dog.who_is_owner())