from amplifier import Amplifier

class AmplifierPipeline:
    def __init__(self, program, phase_settings, feedback_loop_mode = False):
        self.amplifiers = [Amplifier(program, setting) for setting in phase_settings]
        self.feedback_loop_mode = feedback_loop_mode

    def run(self):
        output = 0

        if self.feedback_loop_mode:
            index = 0

            last_amplifier_output = None

            while True:
                output = self.amplifiers[index].start(output)

                if index == len(self.amplifiers) - 1 and output is not None:
                    last_amplifier_output = output

                if output is None:
                    return last_amplifier_output

                index = (index + 1) % len(self.amplifiers)
        else:
            for amplifier in self.amplifiers:
                output = amplifier.start(output)

            return output