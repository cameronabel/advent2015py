def part1():
    with open('day2.txt', 'r') as f:
        presents = f.readlines()
    
    total = 0
    for present in presents:
        l, w, h = [int(dim) for dim in present.split('x')]
        sides = [l * w, l * h, w * h]
        total += 2 * sum(sides) + min(sides)
    return total


def part2():
    with open('day2.txt', 'r') as f:
        presents = f.readlines()
    ribbon = 0
    for present in presents:
        dims = [int(dim) for dim in present.split('x')]
        ribbon += dims[0] * dims[1] * dims[2]
        dims.sort()
        dims.pop()
        ribbon += 2 * sum(dims)

    return ribbon
        
        
print(part1())
print(part2())