from pathlib import Path

with open(Path.home()/'python/project_euler/resources/22.txt') as f:
    names = sorted(f.read().strip().split(','))


def getValue(name):
    total = 0 
    for letter in name:
        if letter != '"':
            total += ord(letter) - 64
    return total

total = 0 

for n in range(len(names)):
    total += getValue(names[n])*(n+1)

print(total)

