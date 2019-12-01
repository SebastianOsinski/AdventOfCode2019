# Part 1

def requiredFuel(mass):
    return mass // 3 - 2

file = open("day1_input", "r")

lines = file.readlines()
masses = [int(l) for l in lines]

modulesFuel = sum([requiredFuel(m) for m in masses])

print(modulesFuel)

# Part 2

def recursiveRequiredFuel(mass):
    fuel = mass // 3 - 2
    if fuel > 0:
        return fuel + recursiveRequiredFuel(fuel)
    else:
        return 0

totalFuel = sum([recursiveRequiredFuel(m) for m in masses])

print(totalFuel)