# OPCODES
ADD = 1
MUL = 2
INP = 3
OUT = 4
JIT = 5
JIF = 6
LES = 7
EQL = 8
HLT = 99

# MODES
POS = 0
IMM = 1

parametersCount = {
    ADD: 3,
    MUL: 3,
    INP: 1,
    OUT: 1,
    JIT: 2,
    JIF: 2,
    LES: 3,
    EQL: 3,
    HLT: 0
}


file = open("day5_input", "r")

line = file.readline()

program = [int(n) for n in line.split(',')]

class Computer:
    def __init__(self, program):
        self.program = program.copy()

    def run(self):
        program = self.program
        counter = 0

        while counter < len(program):
            value = program[counter]
            op = self.opcode(value)

            modes = self.parameterModes(value, parametersCount[op])

            if op == ADD:
                program[program[counter + 3]] = self.parameterValue(counter + 1, modes[0]) + self.parameterValue(counter + 2, modes[1])

                counter += 4
            elif op == MUL:
                program[program[counter + 3]] = self.parameterValue(counter + 1, modes[0]) * self.parameterValue(counter + 2, modes[1])

                counter += 4
            elif op == INP:
                program[program[counter + 1]] = int(input('Input: '))

                counter += 2
            elif op == OUT:
                print(self.parameterValue(counter + 1, modes[0]))

                counter += 2
            elif op == JIT:
                if self.parameterValue(counter + 1, modes[0]) != 0:
                    counter = self.parameterValue(counter + 2, modes[1])
                else:
                    counter += 3
            elif op == JIF:
                if self.parameterValue(counter + 1, modes[0]) == 0:
                    counter = self.parameterValue(counter + 2, modes[1])
                else:
                    counter += 3
            elif op == LES:
                if self.parameterValue(counter + 1, modes[0]) < self.parameterValue(counter + 2, modes[1]):
                    program[program[counter + 3]] = 1
                else:
                    program[program[counter + 3]] = 0
                
                counter += 4
            elif op == EQL:
                if self.parameterValue(counter + 1, modes[0]) == self.parameterValue(counter + 2, modes[1]):
                    program[program[counter + 3]] = 1
                else:
                    program[program[counter + 3]] = 0

                counter += 4
            elif op == HLT:
                break
            else:
                raise Exception(f'Unknown opcode! {op}')

    def opcode(self, value):
        return value % 100
    
    def parameterModes(self, value, count):
        modes = []

        value //= 100

        for i in range(0, count):
            modes.append(value % 10)
            value //= 10

        return modes

    def parameterValue(self, index, mode):
        if mode == POS:
            return self.program[program[index]]
        elif mode == IMM:
            return self.program[index]
        else:
            raise Exception(f'Unknown parameter mode! {mode}')


# Part 1
# Pass 1 when asked for input
computer = Computer(program)
computer.run()

# Part 2
# Pass 5 when asked for input

computer = Computer(program)
computer.run()