def chunks(ls, size):
    for i in range(0, len(ls), size):
        yield ls[i:i + size]

file = open("day8_input", "r")
line = file.readline()

pixels = [int(s) for s in line]

width = 25
height = 6
size = width * height

# Part 1

def count_occurences(layer, pixel):
    return len([p for p in layer if p == pixel])

min_zeros_count = size + 1
count_mult = None

layers = list(chunks(pixels, size))

for layer in layers:
    zeros_count = count_occurences(layer, 0)

    if zeros_count < min_zeros_count:
        min_zeros_count = zeros_count
        count_mult = count_occurences(layer, 1) * count_occurences(layer, 2)

print(count_mult)

# Part 2

BLACK = 0
WHITE = 1
TRANSPARENT = 2

image = list()

for i in range(0, size):
    for layer in layers:
        if layer[i] != TRANSPARENT:
            image.append(layer[i])
            break

assert(len(image) == size)

for r in range(0, height):
    for c in range(0, width):
        pixel = image[r * width + c]

        print("⬛" if pixel == BLACK else "⬜", end='')
    print('')
        
