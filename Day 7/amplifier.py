from computer import Computer

class Amplifier:
    def __init__(self, program, phase_setting):
        self.phase_setting = phase_setting
        self.input_call_count = 0

        self.computer = Computer(program)
        self.computer.input = self.__input

    def start(self, input_signal):
        self.input_signal = input_signal
        
        return self.computer.run()

    def __input(self):
        self.input_call_count += 1

        if self.input_call_count == 1:
            return self.phase_setting
        else:
            return self.input_signal