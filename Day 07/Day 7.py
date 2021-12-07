def part1():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    a = list(map(int, lines[0].split(",")))
    d = dict()
    for i in range(min(a), max(a) + 1):
        c = 0
        for x in a:
            c += abs(x - i)
        d[i] = c
    res = sorted([(k, d[k]) for k in d], key=lambda x: x[1])
    return res[0][1]


def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    a = list(map(int, lines[0].split(",")))
    d = dict()
    for i in range(min(a), max(a) + 1):
        c = 0
        for x in a:
            n = abs(x - i)
            if n > 0:
                c += int((n * (n+1)) / 2)
        d[i] = c
    res = sorted([(k, d[k]) for k in d], key=lambda x: x[1])
    return res[0][1]


if __name__ == "__main__":
    print(part1())
    print(part2())
