def part1():
    with open('puzzle_input.txt', 'r') as f:
        data = f.read()

    floor = 0

    for c in data:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
     
    return floor

def part2():
    with open('puzzle_input.txt', 'r') as f:
        data = f.read()

    floor = 0

    for i, c in enumerate(data, 1):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1:
            return i
     

print(part1())
print(part2())