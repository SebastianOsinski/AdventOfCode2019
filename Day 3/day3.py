file = open("day3_input", "r")

lines = file.readlines()

class Step:
    def __init__(self, string):
        self.direction = string[0]
        self.length = int(string[1:])

    def __repr__(self):
        return f"{self.direction}{self.length}"

class Path:
    def __init__(self, line):
        self.steps = [Step(step) for step in line.split(',')]

    def __repr__(self):
        return self.steps.__repr__()

paths = [Path(line) for line in lines]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattanDistanceFromZero(self):
        return abs(self.x) + abs(self.y)
    
    def __eq__(self, other):
        return other.x == self.x and other.y == self.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"

visitedPointsSets = []
visitedPointsCounters = []

for path in paths:
    currentX = 0
    currentY = 0

    visitedPoints = set()
    stepCounters = dict()

    counter = 0

    for step in path.steps:
        deltaX = 0
        deltaY = 0 
        if step.direction == 'R':
            deltaX = 1
        elif step.direction == 'L':
            deltaX = -1
        elif step.direction == 'U':
            deltaY = 1
        elif step.direction == 'D':
            deltaY = -1
        else:
            raise(Exception('Unknown direction!'))
        
        for i in range(0, step.length):
            currentX += deltaX
            currentY += deltaY

            counter += 1

            point = Point(currentX, currentY)

            visitedPoints.add(point)

            if point not in stepCounters:
                stepCounters[point] = counter

    visitedPointsSets.append(visitedPoints)
    visitedPointsCounters.append(stepCounters)
    
crossings = visitedPointsSets[0].intersection(visitedPointsSets[1])

# Part 1 
print(min(crossing.manhattanDistanceFromZero() for crossing in crossings))

# Part 2
print(min(visitedPointsCounters[0][crossing] + visitedPointsCounters[1][crossing] for crossing in crossings))