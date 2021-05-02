"""
--- Day 1: Not Quite Lisp ---
Santa was hoping for a white Christmas, but his weather machine's "snow" 
function is powered by stars, and he's fresh out! To save Christmas, he needs 
you to collect fifty stars by December 25th.

Collect stars by helping Santa solve puzzles. Two puzzles will be made available 
on each day in the Advent calendar; the second puzzle is unlocked when you 
complete the first. Each puzzle grants one star. Good luck!

Here's an easy puzzle to warm you up.

Santa is trying to deliver presents in a large apartment building, but he can't 
find the right floor - the directions he got are a little confusing. He starts 
on the ground floor (floor 0) and then follows the instructions one character at 
a time.

An opening parenthesis, (, means he should go up one floor, and a closing 
parenthesis, ), means he should go down one floor.

The apartment building is very tall, and the basement is very deep; he will 
never find the top or bottom floors.

For example:

(()) and ()() both result in floor 0.
((( and (()(()( both result in floor 3.
))((((( also results in floor 3.
()) and ))( both result in floor -1 (the first basement level).
))) and )())()) both result in floor -3.
To what floor do the instructions take Santa?

--- Part Two ---
Now, given the same instructions, find the position of the first character that 
causes him to enter the basement (floor -1). The first character in the 
instructions has position 1, the second character has position 2, and so on.

For example:

) causes him to enter the basement at character position 1.
()()) causes him to enter the basement at character position 5.
What is the position of the character that causes Santa to first enter the basement?
"""

def part1():
    """
    Traverses the floors per the instructions in the puzzle input.
    
    Returns:
        
        floor (int) : Santa's final location
    """
    
    with open('day1.txt', 'r') as f:
        data = f.read()

    floor = 0

    for c in data:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
     
    return floor

def part2():
    """
    Traverses the floors per the instructions in the puzzle input.
    
    Returns:
        
        i (int) : The index of the floor instruction that first moves Santa into
            the basement (beginning at index 1)
    """
    
    with open('day1.txt', 'r') as f:
        data = f.read()

    floor = 0

    for i, c in enumerate(data, 1):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1:
            return i
     

def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
