"""
--- Day 5: Doesn't He Have Intern-Elves For This? ---
Santa needs help figuring out which strings in his text file are naughty or nice.

A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or 
aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row, like xx, abcdde 
(dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy, even if they are part of one 
of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a 
double letter (...dd...), and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter, even 
though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
How many strings are nice?

--- Part Two ---
Realizing the error of his ways, Santa has switched to a better model of 
determining whether a string is naughty or nice. None of the old rules apply, as 
they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string 
without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, 
but it overlaps).
It contains at least one letter which repeats with exactly one letter between 
them, like xyx, abcdefeghi (efe), or even aaa.
For example:

qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a 
letter that repeats with exactly one letter between them (zxz).
xxyxx is nice because it has a pair that appears twice and a letter that repeats 
with one between, even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a 
single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between 
(odo), but no pair that appears twice.
How many strings are nice under these new rules?
"""

import re


def nice_vowels(s):
    """Returns True if the string contains at least 3 vowels."""
    matches = re.findall(r'[aeiou]', s)

    return len(matches) >= 3


def nice_combos(s):
    """Returns True if the string does NOT contain ab, cd, pq, or xy."""
    matches = re.findall(r'(ab)|(cd)|(pq)|(xy)', s)
    
    return not matches


def nice_doubles(s):
    """Returns True if the string contains a letter twice in a row."""
    for i, c in enumerate(s[:-1]):
        if c == s[i + 1]:
            return True
    return False


def nice_pairs(s):
    """
    Returns true if the string contains two instances of the same pair of any
    two letters.
    """
    for i, c in enumerate(s[:-2]):
        pair = c + s[i + 1]
        matches = re.findall(pair, s[i + 2:])
        if matches:
            return True
    return False


def nice_sandwich(s):
    """
    Returns True if the string contains any one letter repeated with exactly one 
    letter in between repeats.
    """
    for i, c in enumerate(s[:-2]):
        if c == s[i + 2]:
            return True
    return False


def part1():
    """Counts the strings meeting the criteria for part 1."""
    count = 0
    with open('day5.txt', 'r') as f:
        for s in f:
            count += all((nice_combos(s), nice_doubles(s), nice_vowels(s)))
    return count


def part2():
    """Counts the strings meeting the criteria for part 2."""
    count = 0
    with open('day5.txt', 'r') as f:
        for s in f:
            count += all((nice_pairs(s), nice_sandwich(s)))
    return count
    

def main():
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
