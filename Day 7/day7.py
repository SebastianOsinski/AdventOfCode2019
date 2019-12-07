import itertools

from amplifier_pipeline import AmplifierPipeline

file = open("day7_input", "r")

line = file.readline()

program = [int(n) for n in line.split(',')]

def highest_signal(phase_settings, feedback_loop_mode):
    permutations = list(itertools.permutations(phase_settings))

    max_output = 0
    max_permutation = []

    for permutation in permutations:
        pipeline = AmplifierPipeline(program, permutation, feedback_loop_mode=feedback_loop_mode)

        output = pipeline.run()

        if output > max_output:
            max_output = output
            max_permutation = permutation

    return max_output

# Part 1

print(highest_signal([0, 1, 2, 3, 4], feedback_loop_mode = False))

# Part 2

print(highest_signal([5, 6, 7, 8, 9], feedback_loop_mode = True))