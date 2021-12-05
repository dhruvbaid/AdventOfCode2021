def part1():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    lines = list(map(lambda x: x[:-1].split(" -> "), lines))
    d = dict()
    for l in lines:
        sX, sY = list(map(int, l[0].split(",")))
        eX, eY = list(map(int, l[1].split(",")))
        if sX == eX:
            if sY <= eY:
                points = [(sX, sY + dY) for dY in range(eY - sY + 1)]
            else:
                points = [(sX, sY + dY) for dY in range(eY - sY, 1)]
            for p in points:
                if p in d:
                    d[p] += 1
                else:
                    d[p] = 1
        elif sY == eY:
            if sX <= eX:
                points = [(sX + dX, sY) for dX in range(eX - sX + 1)]
            else:
                points = [(sX + dX, sY) for dX in range(eX - sX, 1)]
            for p in points:
                if p in d:
                    d[p] += 1
                else:
                    d[p] = 1
        else:
            continue
    return len(list(filter(lambda x: x[1] >= 2, zip(d.keys(), d.values()))))


def part2():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    lines = list(map(lambda x: x[:-1].split(" -> "), lines))
    d = dict()
    for l in lines:
        # print(l)
        sX, sY = list(map(int, l[0].split(",")))
        eX, eY = list(map(int, l[1].split(",")))
        if sX == eX:
            if sY <= eY:
                points = [(sX, sY + dY) for dY in range(eY - sY + 1)]
            else:
                points = [(sX, sY + dY) for dY in range(eY - sY, 1)]
            # print(points)
            for p in points:
                if p in d:
                    d[p] += 1
                else:
                    d[p] = 1
        elif sY == eY:
            if sX <= eX:
                points = [(sX + dX, sY) for dX in range(eX - sX + 1)]
            else:
                points = [(sX + dX, sY) for dX in range(eX - sX, 1)]
            # print(points)
            for p in points:
                if p in d:
                    d[p] += 1
                else:
                    d[p] = 1
        else:
            # diagonal cases
            if sX <= eX:
                diffX = range(eX - sX + 1)
            else:
                diffX = range(0, eX - sX - 1, -1)

            if sY <= eY:
                diffY = range(eY - sY + 1)
            else:
                diffY = range(0, eY - sY - 1, -1)

            for dX, dY in zip(diffX, diffY):
                p = (sX + dX, sY + dY)
                if p in d:
                    d[p] += 1
                else:
                    d[p] = 1
    return len(list(filter(lambda x: x[1] >= 2, zip(d.keys(), d.values()))))


if __name__ == "__main__":
    print(part1())
    print(part2())