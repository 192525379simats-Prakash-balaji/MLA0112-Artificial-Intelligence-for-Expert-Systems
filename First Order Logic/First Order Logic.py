humans = {"socrates", "plato", "aristotle"}

def human(x):
    return x in humans

def mortal(x):
    return human(x)

person = "socrates"

if mortal(person):
    print(person, "is mortal")