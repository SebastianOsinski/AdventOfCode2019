# OPCODES
ADD = 1
MUL = 2
INP = 3
OUT = 4
JIT = 5
JIF = 6
LES = 7
EQL = 8
ARB = 9
HLT = 99

# MODES
POS = 0
IMM = 1
REL = 2

PARAMETERS_COUNT = {
    ADD: 3,
    MUL: 3,
    INP: 1,
    OUT: 1,
    JIT: 2,
    JIF: 2,
    LES: 3,
    EQL: 3,
    ARB: 1,
    HLT: 0
}

class Computer:
    def __init__(self, program):
        self.memory = program.copy()
        self.input = None
        self.counter = 0
        self.relative_base = 0

    def run(self):
        while True:
            value = self.__memory_value(self.counter)
            op = self.__opcode(value)

            modes = self.__parameter_modes(value, PARAMETERS_COUNT[op])

            if op == ADD:
                result = \
                    self.__parameter_value(self.counter + 1, modes[0]) + \
                    self.__parameter_value(self.counter + 2, modes[1])

                self.__write(self.counter + 3, modes[2], result)

                self.counter += 4
            elif op == MUL:
                result = \
                    self.__parameter_value(self.counter + 1, modes[0]) * \
                    self.__parameter_value(self.counter + 2, modes[1])

                self.__write(self.counter + 3, modes[2], result)

                self.counter += 4
            elif op == INP:
                self.__write(self.counter + 1, modes[0], self.input())

                self.counter += 2
            elif op == OUT:
                output = self.__parameter_value(self.counter + 1, modes[0])
                self.counter += 2

                yield output
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
                    self.__write(self.counter + 3, modes[2], 1)
                else:
                    self.__write(self.counter + 3, modes[2], 0)

                self.counter += 4
            elif op == EQL:
                if self.__parameter_value(self.counter + 1, modes[0]) == self.__parameter_value(self.counter + 2, modes[1]):
                    self.__write(self.counter + 3, modes[2], 1)
                else:
                    self.__write(self.counter + 3, modes[2], 0)

                self.counter += 4
            elif op == ARB:
                self.relative_base += self.__parameter_value(self.counter + 1, modes[0])
                self.counter += 2
            elif op == HLT:
                return
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

    def __write(self, index, mode, value):
        final_index = None

        self.__increase_memory_size(index)

        if mode == POS:
            final_index = self.memory[index]
        elif mode == REL:
            final_index = self.relative_base + self.memory[index]
        else:
            return Exception(f'Unsupported write mode! {mode}')

        self.__increase_memory_size(final_index)

        self.memory[final_index] = value

    def __memory_value(self, index):
        self.__increase_memory_size(index)
        return self.memory[index]

    def __increase_memory_size(self, up_to):
        if len(self.memory) <= up_to:
            self.memory.extend([0] * (up_to + 1 - len(self.memory)))

    def __parameter_value(self, index, mode):
        if mode == POS:
            return self.__memory_value(self.__memory_value(index))
        elif mode == IMM:
            return self.__memory_value(index)
        elif mode == REL:
            return self.__memory_value(self.relative_base + self.__memory_value(index))
        else:
            raise Exception(f'Unknown parameter mode! {mode}')
