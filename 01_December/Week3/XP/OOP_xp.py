# OOP Exercises 1–4 (Inheritance + Classes) — copy/paste once
import random

print("\n" + "=" * 60)
print("EXERCISE 1: Pets (Cats + Inheritance)")
print("=" * 60 + "\n")

class Pets:
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat:
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f"{self.name} is just walking around"


class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"


class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# Step 1: Create Siamese class
class Siamese(Cat):
    # No unique behavior required for the exercise; inherits everything from Cat
    pass


# Step 2: Create a list of cat instances
bengal_obj = Bengal("Nala", 3)
chartreux_obj = Chartreux("Mochi", 6)
siamese_obj = Siamese("Blue", 4)

all_cats = [bengal_obj, chartreux_obj, siamese_obj]

# Step 3: Create a Pets instance
sara_pets = Pets(all_cats)

# Step 4: Take cats for a walk
sara_pets.walk()


print("\n" + "=" * 60)
print("EXERCISE 2: Dogs (bark, run_speed, fight)")
print("=" * 60 + "\n")

class Dog:
    def __init__(self, name, age, weight):
        self.name = name      # string
        self.age = age        # number
        self.weight = weight  # number

    def bark(self):
        return f"{self.name} is barking"

    def run_speed(self):
        # weight / age * 10
        return (self.weight / self.age) * 10

    def fight(self, other_dog):
        # winner based on: run_speed * weight
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight

        if my_power > other_power:
            return f"{self.name} won the fight against {other_dog.name}!"
        elif other_power > my_power:
            return f"{other_dog.name} won the fight against {self.name}!"
        else:
            return f"It's a tie between {self.name} and {other_dog.name}!"


# Step 2: Create dog instances
dog1 = Dog("Rocky", 5, 24)
dog2 = Dog("Bella", 3, 18)
dog3 = Dog("Max", 4, 22)

# Step 3: Test methods
print(dog1.bark())
print(f"{dog1.name} run speed: {dog1.run_speed():.2f}")
print(dog1.fight(dog2))
print(dog2.fight(dog3))


print("\n" + "=" * 60)
print("EXERCISE 3: PetDog (Inheritance + training + tricks)")
print("=" * 60 + "\n")

class PetDog(Dog):
    def __init__(self, *args, trained=False, **kwargs):
        super().__init__(*args, **kwargs)
        self.trained = trained

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *other_dogs):
        # other_dogs should be Dog/PetDog objects
        names = [self.name] + [dog.name for dog in other_dogs]
        print(f"{', '.join(names)} all play together")

    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead",
            ]
            print(f"{self.name} {random.choice(tricks)}")
        else:
            print(f"{self.name} is not trained yet.")


# Step 3: Test PetDog methods
fido = PetDog("Fido", 2, 10)
buddy = PetDog("Buddy", 4, 20)
luna = PetDog("Luna", 1, 7)

fido.do_a_trick()      # not trained yet
fido.train()           # sets trained = True
fido.do_a_trick()      # now can do tricks
fido.play(buddy, luna) # *args demo


print("\n" + "=" * 60)
print("EXERCISE 4: Family and Person Classes")
print("=" * 60 + "\n")

class Person:
    def __init__(self, first_name, age, last_name=""):
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def is_18(self):
        return self.age >= 18


class Family:
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):
        new_person = Person(first_name, age, self.last_name)
        self.members.append(new_person)

    def check_majority(self, first_name):
        for person in self.members:
            if person.first_name == first_name:
                if person.is_18():
                    print(
                        f"You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )
                else:
                    print("Sorry, you are not allowed to go out with your friends.")
                return
        print(f"No family member named {first_name} was found.")

    def family_presentation(self):
        print(f"Family last name: {self.last_name}")
        for person in self.members:
            print(f"{person.first_name}, {person.age}")


# Example usage / expected behavior
my_family = Family("Smith")
my_family.born("Alice", 16)
my_family.born("Bob", 19)

my_family.family_presentation()
my_family.check_majority("Alice")
my_family.check_majority("Bob")
my_family.check_majority("Charlie")
