def invalid(i, aMin, aMax):
    return i[1] < aMin or i[0] > aMax


def tripletInvalid(instructions, aMin, aMax):
    for i in instructions:
        if invalid(i, aMin, aMax):
            return True
    return False


def intersect(p1, p2):
    return max(p1[0], p2[0]), min(p1[1], p2[1])


def part1(instructions):
    d = dict()
    for i in instructions:
        if tripletInvalid((i[1], i[2], i[3]), -50, 50):
            continue
        else:
            xRange = intersect(i[1], (-50, 50))
            yRange = intersect(i[2], (-50, 50))
            zRange = intersect(i[3], (-50, 50))
            for x in range(xRange[0], xRange[1] + 1):
                for y in range(yRange[0], yRange[1] + 1):
                    for z in range(zRange[0], zRange[1] + 1):
                        d[(x, y, z)] = i[0]
    return sum(d.values())


def part2(instructions):
    d = []
    for iNum, i in enumerate(instructions):
        print(f"Instruction {iNum}!")
        xRange = i[1]
        yRange = i[2]
        zRange = i[3]
        if i[0] == 1:
            for x in range(xRange[0], xRange[1] + 1):
                for y in range(yRange[0], yRange[1] + 1):
                    for z in range(zRange[0], zRange[1] + 1):
                        d.append((x, y, z))
        else:
            if (x, y, z) in d:
                d.remove((x, y, z))
    return len(d)


if __name__ == "__main__":
    # Parse input
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    instructions = []
    for l in lines:
        if '\n' in l:
            l = l[:-1]
        if l[:2] == "on":
            tmp = l[3:].split(",")
            for i, x in enumerate(tmp):
                x = x[2:].split("..")
                tmp[i] = (int(x[0]), int(x[1]))
            instructions.append((1, tmp[0], tmp[1], tmp[2]))
        else:
            tmp = l[4:].split(",")
            for i, x in enumerate(tmp):
                x = x[2:].split("..")
                tmp[i] = (int(x[0]), int(x[1]))
            instructions.append((0, tmp[0], tmp[1], tmp[2]))


    # Evaluate parts 1 and 2
    print(part1(instructions))
    # print(part2(instructions))

