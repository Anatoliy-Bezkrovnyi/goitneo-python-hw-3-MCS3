class Animal:
    color = "white"

    def __init__(self, nickname, weight ) -> None:
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, new_weight):
        self.weight = new_weight

    def change_color(self, color):
        Animal.color = color

first_animal  = Animal("Simon", 10)
second_animal = Animal("Marly", 5)
second_animal.change_color("red")

print(first_animal.nickname)
print(second_animal.nickname)
print(Animal.color)
        