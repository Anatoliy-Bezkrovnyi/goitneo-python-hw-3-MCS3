class Animal:
    color = "white"

    def __init__(self, nickname, weight ) -> None:
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

class Cat(Animal):

    def say(self):
        print("Meow")
    
cat = Cat("Simon", 10)
cat.say()