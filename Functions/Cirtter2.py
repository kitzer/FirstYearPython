class Critter(object):
    """ Pet """
    
    def __init__(self):
        print("A new cirtter has been born")

    def talk(self):
        print("\nHi. I'm an instance of class Critter.")


# Main Program
crit1 = Critter()
crit2 = Critter()

crit1.talk()
crit2.talk()



