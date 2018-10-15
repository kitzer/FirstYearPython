class Critter(object):
    """ Pet """
    def __init__(self, name):
        print("A new critter has been born.")
        self.name = name

    def __str__(self):
        rep = "Critter object\n"
        rep += "name: " + self.name + "\n"

        return rep

    def talk(self):
        print("Hi. I'm", self.name, "\n")

# Main program
crit1 = Critter("Poochie")
crit1.talk()

crit2 = Critter("Randoplh")
crit2.talk()

print("Printing crit1:")
print(crit1)

print("Directly accessing crit1.name:")
print(crit1.name)


