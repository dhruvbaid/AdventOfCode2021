def part1():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    dots = []
    folds = []
    isDot = True
    for l in lines:
        if isDot:
            tmp = l[:-1].split(",")
            if tmp != ['']:
                dots.append((int(tmp[0]), int(tmp[1])))
        if l == "\n":
            isDot = False
        if not isDot:
            if '\n' in l:
                l = l[:-1]
            if l != '':
                tmp = l[11:].split("=")
                folds.append((tmp[0], int(tmp[1])))
    # print(dots)
    # print(folds)
    f = folds[0]
    if f[0] == 'x':
        a = []
        for x in dots:
            if x[0] > f[1]:
                a.append((2*f[1] - x[0], x[1]))
            else:
                a.append(x)
        return len(set(a))
    else:
        a = []
        for x in dots:
            if x[1] > f[1]:
                a.append((x[0], 2*f[1] - x[1]))
            else:
                a.append(x)
        return len(set(a))


def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    dots = []
    folds = []
    isDot = True
    for l in lines:
        if isDot:
            tmp = l[:-1].split(",")
            if tmp != ['']:
                dots.append((int(tmp[0]), int(tmp[1])))
        if l == "\n":
            isDot = False
        if not isDot:
            if '\n' in l:
                l = l[:-1]
            if l != '':
                tmp = l[11:].split("=")
                folds.append((tmp[0], int(tmp[1])))
    # print(dots)
    # print(folds)
    for f in folds:
        a = []
        if f[0] == 'x':
            for x in dots:
                if x[0] > f[1]:
                    a.append((2*f[1] - x[0], x[1]))
                else:
                    a.append(x)
        else:
            for x in dots:
                if x[1] > f[1]:
                    a.append((x[0], 2*f[1] - x[1]))
                else:
                    a.append(x)
        dots = [_ for _ in a]
    xMax = max(list(map(lambda x: x[0], dots)))
    yMax = max(list(map(lambda x: x[1], dots)))
    for i in range(yMax + 1):
        for j in range(xMax + 1):
            if (j, i) in dots:
                print("#", end='')
            else:
                print(" ", end='')
        print("\n", end='')
    return 0


if __name__ == "__main__":
    print(part1())
    print(part2())
