
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(f"arthur.hp = {arthur.hp}")     # Expected: 90
print(f"morgana.hp = {morgana.hp}")    # Expected: 100


# this is sodium