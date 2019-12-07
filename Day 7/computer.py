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

PARAMETERS_COUNT = {
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

class Computer:
    def __init__(self, program):
        self.program = program.copy()
        self.input = None
        self.counter = 0

    def run(self):
        program = self.program
        
        while self.counter < len(program):
            value = program[self.counter]
            op = self.__opcode(value)

            modes = self.__parameter_modes(value, PARAMETERS_COUNT[op])

            if op == ADD:
                program[program[self.counter + 3]] = \
                    self.__parameter_value(self.counter + 1, modes[0]) + \
                    self.__parameter_value(self.counter + 2, modes[1])

                self.counter += 4
            elif op == MUL:
                program[program[self.counter + 3]] = \
                    self.__parameter_value(self.counter + 1, modes[0]) * \
                    self.__parameter_value(self.counter + 2, modes[1])

                self.counter += 4
            elif op == INP:
                program[program[self.counter + 1]] = self.input()

                self.counter += 2
            elif op == OUT:
                output = self.__parameter_value(self.counter + 1, modes[0])
                self.counter += 2

                return output
            elif op == JIT:
                if self.__parameter_value(self.counter + 1, modes[0]) != 0:
                    self.counter = self.__parameter_value(self.counter + 2, modes[1])
                else:
                    self.counter += 3
            elif op == JIF:
                if self.__parameter_value(self.counter + 1, modes[0]) == 0:
                    self.counter = self.__parameter_value(self.counter + 2, modes[1])
                else:
                    self.counter += 3
            elif op == LES:
                if self.__parameter_value(self.counter + 1, modes[0]) < self.__parameter_value(self.counter + 2, modes[1]):
                    program[program[self.counter + 3]] = 1
                else:
                    program[program[self.counter + 3]] = 0

                self.counter += 4
            elif op == EQL:
                if self.__parameter_value(self.counter + 1, modes[0]) == self.__parameter_value(self.counter + 2, modes[1]):
                    program[program[self.counter + 3]] = 1
                else:
                    program[program[self.counter + 3]] = 0

                self.counter += 4
            elif op == HLT:
                return None
            else:
                raise Exception(f'Unknown opcode! {op}')

    def __opcode(self, value):
        return value % 100

    def __parameter_modes(self, value, count):
        modes = []

        value //= 100

        for i in range(0, count):
            modes.append(value % 10)
            value //= 10

        return modes

    def __parameter_value(self, index, mode):
        if mode == POS:
            return self.program[self.program[index]]
        elif mode == IMM:
            return self.program[index]
        else:
            raise Exception(f'Unknown parameter mode! {mode}')
