ADD = 1
MULT = 2
HLT = 99

file = open("day2_input", "r")

line = file.readline()

program = [int(n) for n in line.split(',')]

class Computer:
    def __init__(self, program, input1, input2):
        self.program = program.copy()
        self.program[1] = input1
        self.program[2] = input2

    def run(self):
        program = self.program
        counter = 0

        while counter < len(program):
            op = program[counter]

            if op == ADD:
                program[program[counter + 3]] = program[program[counter + 1]] + program[program[counter + 2]]
                counter += 4
            elif op == MULT:
                program[program[counter + 3]] = program[program[counter + 1]] * program[program[counter + 2]]
                counter += 4
            elif op == HLT:
                break
            else:
                raise Exception(f'Unknown opcode! {op}')

        return program[0]

    
computer = Computer(program, 12, 2)

# Part 1
print(computer.run())

# Part 2

desiredOutput = 19690720

for noun in range(0, 100):
    for verb in range(0, 100):
        output = Computer(program, noun, verb).run()

        if output == desiredOutput:
            print(100 * noun + verb)
            break