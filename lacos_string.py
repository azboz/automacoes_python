import time

data = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z', 'w'
]

for i in range(0, len(data)):

    for y in range(0, len(data)):
        print(data[i], data[y], end="")
