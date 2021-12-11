def neighbors(i, j, a):
    """
    Find the neighbors of a given element in an array
    :param i: input element's row
    :param j: input element's column
    :param a: input array
    :return: list of indices of a[i][j]'s neighbors
    """
    r = len(a)
    c = len(a[0])
    v = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return [(i+dx, j+dy) for dx, dy in v if 0 <= i+dx < r and 0 <= j+dy < c]


def step(a):
    numFlashes = 0
    for i, l in enumerate(a):
        a[i] = list(map(lambda x: x + 1, l))
    while len(list(filter(lambda x: len(list(filter(lambda y: y > 9, x))), a))) != 0:
        flashed = []
        flag = True
        while flag:
            newFlash = []
            flag = False
            for i in range(len(a)):
                for j in range(len(a[0])):
                    if a[i][j] > 9:
                        flag = True
                        newFlash.append((i, j))
                        a[i][j] = 0
                        numFlashes += 1
            flashed += newFlash
            for i, j in newFlash:
                for i2, j2 in neighbors(i, j, a):
                    if (i2, j2) not in flashed:
                        a[i2][j2] += 1
    return a, numFlashes


def part1():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    for i, l in enumerate(lines):
        if '\n' in l:
            l = l[:-1]
        lines[i] = list(map(int, l))
    totalFlashes = 0
    for _ in range(100):
        lines, numFlashes = step(lines)
        totalFlashes += numFlashes
    return totalFlashes


def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    for i, l in enumerate(lines):
        if '\n' in l:
            l = l[:-1]
        lines[i] = list(map(int, l))
    flashNum = 0
    numOct = len(lines) * len(lines[0])
    while True:
        lines, numFlashes = step(lines)
        flashNum += 1
        if numFlashes == numOct:
            return flashNum


if __name__ == "__main__":
    print(part1())
    print(part2())
