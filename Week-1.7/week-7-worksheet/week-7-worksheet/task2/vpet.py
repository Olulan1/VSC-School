# Define a class called VirtualPet with the following attributes:
# (1) name - the name of the pet
# (2) energy - the energy points for the pet, default value is 10
# (3) hunger - the pet's hunger level, default value is 0
# When an instance of VirtualPet is created, only the name is needed, as a minimum, for the __init__ method

class VirtualPet(): # class name
    def __init__(self, name="", energy=10, hunger=0): # default args
        self.name = name
        self.energy = energy
        self.hunger = hunger
    
    def play(self):
        if self.energy >= 2: # option validation
            self.energy-=2
            self.hunger+=2
        else:
            return (f"{self.name} is too tired to play!")
    
    def feed(self):
        self.hunger-=3
        if self.hunger <0:
            self.hunger = 0
            return (f"{self.name} is overfed!") # check for overfeeding, no need to check for underfeeding

    def sleep(self):
        self.energy+=10

    def __str__(self):
       return (f"{self.name} has {self.energy} energy points and hunger level {self.hunger}")
    
    def __eq__(self, other):
        if self.name == other.name:
            if self.energy == other.energy:
                if self.hunger == other.hunger:
                    return True
                else:
                    return False
            else:
                    return False
        else:
                    return False

Pet = VirtualPet("Timmy", 2, 3)
Pet.play()
Pet.play()
Pet.play()
Pet.play()