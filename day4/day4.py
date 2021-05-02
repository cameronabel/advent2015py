"""
--- Day 4: The Ideal Stocking Stuffer ---
Santa needs help mining some AdventCoins (very similar to bitcoins) to use as 
gifts for all the economically forward-thinking little girls and boys.

To do this, he needs to find MD5 hashes which, in hexadecimal, start with at 
least five zeroes. The input to the MD5 hash is some secret key (your puzzle 
input, given below) followed by a number in decimal. To mine AdventCoins, you 
must find Santa the lowest positive number (no leading zeroes: 1, 2, 3, ...) 
that produces such a hash.

For example:

If your secret key is abcdef, the answer is 609043, because the MD5 hash of 
abcdef609043 starts with five zeroes (000001dbbfa...), and it is the lowest 
such number to do so.
If your secret key is pqrstuv, the lowest number it combines with to make an MD5 
hash starting with five zeroes is 1048970; that is, the MD5 hash of 
pqrstuv1048970 looks like 000006136ef....

--- Part Two ---
Now find one that starts with six zeroes.


Your puzzle input was bgvyzdsv.
"""

import hashlib


key = 'bgvyzdsv'

def part1(key):
    """
    Increments a numerical value to append to the given key, then returns the 
    value that produces an MD5 hash beginning with 5 zeroes.
    
    Parameters
    ----------
        key (str) : the leading string to be hashed
        
    Returns
    -------
        num (int) : the number that, when appended to the key, produces a hash
            beginning with 5 zeroes
    """
    
    num = 0
    while True:
        s = key + str(num)
        result = hashlib.md5(s.encode())
        if result.hexdigest().startswith('00000'):
            return num
        num += 1


def part2(key):
    """
    Increments a numerical value to append to the given key, then returns the 
    value that produces an MD5 hash beginning with 6 zeroes.
    
    Parameters
    ----------
        key (str) : the leading string to be hashed
        
    Returns
    -------
        num (int) : the number that, when appended to the key, produces a hash
            beginning with 6 zeroes
    """
    
    num = 0
    while True:
        s = key + str(num)
        result = hashlib.md5(s.encode())
        if result.hexdigest().startswith('000000'):
            return num
        num += 1
        
        
def main():
    print(part1(key))
    print(part2(key))


if __name__ == '__main__':
    main()
