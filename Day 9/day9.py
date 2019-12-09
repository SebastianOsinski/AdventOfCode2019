from computer import Computer

file = open("day9_input", "r")

line = file.readline()

program = [int(n) for n in line.split(',')]


# Part 1

computer = Computer(program)
computer.input = (lambda: 1)

for output in computer.run():
    print(output)

# Part 2

computer = Computer(program)
computer.input = (lambda: 2)

for output in computer.run():
    print(output)