def nice_vowels(s):
    count = 0
    for vowel in 'aeiou':
        count += s.count(vowel)
        if count >= 3:
            return True
    return False


def nice_doubles(s):
    for char in set(s):
        if char + char in s:
            return True
    return False


def nice_combos(s):
    for combo in ['ab', 'cd', 'pq', 'xy']:
        if combo in s:
            return False
    return True

def part1(puzzle):
    count = 0
    with open(puzzle, 'r') as f:
        for s in f:
            count += all((nice_combos(s), nice_doubles(s), nice_vowels(s)))
    return count


print(part1('day5.txt'))