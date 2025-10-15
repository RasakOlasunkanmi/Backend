# create a simple class names Pet.
# This class should have features name, species and age.
# Include a function to display the class information.
# Write a function to celebrate the pet's birthday.


class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Species: {self.species}, Age: {self.age}"

    def celebrate_birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."
if __name__ == "__main__":
    my_pet = Pet("Bruno", "Dog", 5)
    print(my_pet.display_info())
    print(my_pet.celebrate_birthday())
    print(my_pet.display_info())

    
    