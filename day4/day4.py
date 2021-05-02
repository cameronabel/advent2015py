import hashlib


key = 'bgvyzdsv'

def part1(key):
    num = 0
    while True:
        s = key + str(num)
        result = hashlib.md5(s.encode())
        if result.hexdigest().startswith('00000'):
            return num
        num += 1

def part2(key):
    num = 0
    while True:
        s = key + str(num)
        result = hashlib.md5(s.encode())
        if result.hexdigest().startswith('000000'):
            return num
        num += 1

print(part1(key))
print(part2(key))