# Define a class called VirtualPet with the following attributes:
# (1) name - the name of the pet
# (2) energy - the energy points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is needed, as a minimum, for the __init__ method

class VirtualPet:

    def _init_(self, petName, energy = 10, hunger = 0 ):
        self.petName = petName
        self.energy = energy
        self.hunger = hunger
    
    def play(self):
        if self.energy < 2:
            print(f"{self.petName} is too tired to play!")
        else:
            self.energy-=2
            self.hunger-=self.hunger - 2
    
    def feed(self):
        if self.hunger < 0:
            print(f"{self.petName} is overfed!")
        else:
            self.hunger-=-3
    
    def sleep(self):
        self.energy+=10

    def __str__(self):
        details = f"{self.petName} has {self.energy} energy points and hunger level{self.hunger}"
        return details
    
    def __eq__(self, value):
        if (self.energy == self.hunger):
            value = True
        else:
            value = False
        return value


Pet = VirtualPet("Timmy", 0, 0)

# This class has the following methods:
# (1) play() - If energy<2, report in the format "{name} is too tired to play!".
#     Otherwise simulate playing by reducing the energy by 2 and increase the hunger by 2.
# (2) feed() - Simulate feeding the pet and reducing hunger by 3.
#     If hunger is less than 0, report in the format "{name} is overfed!" and reset hunger to 0.
# (3) sleep() - let the pet sleep and increase the energy by 10.
# (4) __str__() - returns the details of the pet in the format "{name} has {energy} energy points and hunger level {hunger}", 
#     e.g., "Timmy has 100 energy points and hunger level 0"
# (5) __eq__() - returns True if all attributes are identical, False otherwise

# You should test each method in your code before submission.
# Check that attributes are modified as expected
# For example:

