class Relationship:
    def __init__(self, line):
        objects = line.split(')')
        self.orbitee = objects[0]
        self.orbiter = objects[1]

    def __repr__(self):
        return f'{self.orbitee}){self.orbiter}'

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = set()
    
    def add_child(self, child):
        assert(child.parent is None)

        self.children.add(child)
        child.parent = self

    def levels_sum(self):
        return self.__levels_sum(0)

    def __repr__(self):
        return self.__recursive_repr(1)

    def __recursive_repr(self, indent_level):
        indentation = ' ' * indent_level
        lines = []
        if len(self.children) == 0:
            lines.append(indentation + self.name)
        else:
            lines.append(indentation + self.name + ' -> {')
            for child in self.children:
                lines.append(child.__recursive_repr(indent_level + 1))
            
            lines.append(indentation + '}')

        return "\n".join(lines)

    def __levels_sum(self, level):
        return level + sum(child.__levels_sum(level + 1) for child in self.children)

class NodePool:
    def __init__(self):
        self.pool = dict()

    def node(self, name):
        return self.pool.setdefault(name, Node(name))

    def min_orbital_transfers(self, first_node_name, second_node_name):
        first_parent = self.pool[first_node_name]
        second_parent = self.pool[second_node_name]

        first_parent_dist = dict()
        second_parent_dist = dict()

        first_counter = 0
        second_counter = 0

        def sum_dist(node):
            return first_parent_dist[node] + second_parent_dist[node]

        while True:
            first_parent = first_parent.parent
            second_parent = second_parent.parent

            first_parent_dist[first_parent] = first_counter
            second_parent_dist[second_parent] = second_counter

            first_counter += 1
            second_counter += 1

            if first_parent is None or second_parent is None:
                return None

            if first_parent == second_parent or first_parent in second_parent_dist:
                return sum_dist(first_parent)
            elif second_parent in first_parent_dist:
                return sum_dist(second_parent)

file = open("day6_input", "r")
lines = file.read().splitlines()

relationships = [Relationship(line) for line in lines]

node_pool = NodePool()

for relationship in relationships:
    orbitee_node = node_pool.node(relationship.orbitee)
    orbiter_node = node_pool.node(relationship.orbiter)

    orbitee_node.add_child(orbiter_node)

# Part 1
print(node_pool.node('COM').levels_sum())

# Part 2
print(node_pool.min_orbital_transfers('YOU', 'SAN'))