
class PSHS_Galaxy:
    def introduce(self):
        print("Welcome to PSHS Galaxy!")

    def identity(self):
        print("I am a student.")


class Nationality:
    def introduce(self):
        print("Hello!")

    def identity(self):
        print("I have a nationality.")


class Filipino(Nationality):
    def identity(self):
        super().identity()
        print("I am a Filipino.")


class Indonesians(Nationality):
    def identity(self):
        super().identity()
        print("I am an Indonesian.")


class Spaniards(Nationality):
    def identity(self):
        super().identity()
        print("I am a Spaniard.")


class Alien:
    def introduce(self):
        print("Greetings, Earthlings!")

    def identity(self):
        print("I am an alien.")


class Marvel(Alien):
    def identity(self):
        super().identity()
        print("I belong to Marvel.")


class Avengers(Marvel):
    def identity(self):
        super().identity()
        print("I am an Avenger.")


objects = [
    PSHS_Galaxy(),
    Filipino(),
    Indonesians(),
    Spaniards(),
    Alien(),
    Marvel(),
    Avengers()
]

for obj in objects:
    obj.introduce()
    obj.identity()
    print()
