def part1():
    with open('day3.txt', 'r') as f:
        dirs = f.read()
    
    pos = 0, 0
    visited = {pos}
    for dir in dirs:
        if dir == '^':
            pos = pos[0], pos[1] + 1
        elif dir == '>':
            pos = pos[0] + 1, pos[1]
        elif dir == 'v':
            pos = pos[0], pos[1] - 1
        elif dir == '<':
            pos = pos[0] - 1, pos[1]
        
        visited.add(pos)
    
    return len(visited)


def part2():
    with open('day3.txt', 'r') as f:
        dirs = f.read()
    
    visited = {(0, 0)}
    for i in range(2):
        pos = 0, 0
        for dir in dirs[i::2]:
            if dir == '^':
                pos = pos[0], pos[1] + 1
            elif dir == '>':
                pos = pos[0] + 1, pos[1]
            elif dir == 'v':
                pos = pos[0], pos[1] - 1
            elif dir == '<':
                pos = pos[0] - 1, pos[1]
        
            visited.add(pos)
    
    return len(visited)


print(part1())
print(part2())