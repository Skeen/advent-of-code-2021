from itertools import starmap
from operator import lt
from more_itertools import pairwise


def count_increasing(numbers):
    pairs = pairwise(numbers)
    increasing = starmap(lt, pairs)
    return sum(increasing)


test = [
    199, 200, 208, 210, 200, 207, 240, 269, 260, 263
]
print(count_increasing(test))
assert count_increasing(test) == 7


with open("input", "r") as in_file:
    lines = in_file.readlines()
numbers = map(int, lines)
numbers = list(numbers)


print(count_increasing(numbers))


from more_itertools import triplewise
triplets = triplewise(numbers)
triplets = map(sum, triplets)

print(count_increasing(triplets))
