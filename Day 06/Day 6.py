def update(d):
    a = d[0] if 0 in d else 0
    for i in range(8):
        d[i] = d[i + 1]
    d[6] += a
    d[8] = a
    return d

def part1():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    a = list(map(int, lines[0].split(",")))
    d = {i: a.count(i) for i in range(9)}
    for _ in range(80):
        d = update(d)
    return sum(d.values())

def part2():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    a = list(map(int, lines[0].split(",")))
    d = {i: a.count(i) for i in range(9)}
    print(d)
    for _ in range(256):
        d = update(d)
        # print(d)
    return sum(d.values())


if __name__ == "__main__":
    print(part1())
    print(part2())