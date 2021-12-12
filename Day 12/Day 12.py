def findPaths(d):
    paths = [(['start'], [])]
    finalPaths = []
    while len(paths) != 0:
        newPaths = []
        for i, pv in enumerate(paths):
            p = pv[0]
            next = d[p[-1]]
            for n in next:
                if n == 'end':
                    tmp = p + [n]
                    finalPaths.append(tmp)
                    # print(f"finalPaths = {finalPaths}")
                else:
                    if n not in pv[1] and n != 'start':
                        tmp = p + [n]
                        # print(f"tmp = {tmp}")
                        t2 = pv[1] + [n] if n.islower() else pv[1]
                        newPaths.append((tmp, t2))
        # print(f"newPaths = {newPaths}")
        paths = newPaths
        # print(f"paths = {paths}")
    # print(f"finalPaths = {finalPaths}")
    return finalPaths

def isValid(p):
    count = 0
    for x in list(filter(lambda x: x.islower(), list(set(p)))):
        if p.count(x) >= 2:
            count += 1
        if count >= 2:
            # print(p, " failed")
            return False
    return True


def findPaths2(d):
    paths = [(['start'], [])]
    finalPaths = []
    while len(paths) != 0:
        newPaths = []
        for i, pv in enumerate(paths):
            # print(pv[1])
            p = pv[0]
            next = d[p[-1]]
            for n in next:
                if n == 'end':
                    tmp = p + [n]
                    finalPaths.append(tmp)
                    # print(f"finalPaths = {finalPaths}")
                else:
                    if n != 'start' and pv[1].count(n) < 2:
                        tmp = p + [n]
                        # print(f"tmp = {tmp}")
                        t2 = pv[1] + [n] if n.islower() else pv[1]
                        if isValid(tmp):
                            newPaths.append((tmp, t2))
        # print(f"newPaths = {newPaths}")
        paths = newPaths
        # print(f"paths = {paths}")
    # print(f"finalPaths = {finalPaths}")
    return finalPaths

def part1():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    a = []
    for i, l in enumerate(lines):
        if '\n' in l:
            lines[i] = lines[i][:-1]
        a.append(lines[i].split("-"))
    d = dict()
    for x in a:
        if x[0] in d:
            d[x[0]].append(x[1])
        else:
            d[x[0]] = [x[1]]

        if x[1] in d:
            d[x[1]].append(x[0])
        else:
            d[x[1]] = [x[0]]
    # print(d)
    return len(findPaths(d))

def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    a = []
    for i, l in enumerate(lines):
        if '\n' in l:
            lines[i] = lines[i][:-1]
        a.append(lines[i].split("-"))
    d = dict()
    for x in a:
        if x[0] in d:
            d[x[0]].append(x[1])
        else:
            d[x[0]] = [x[1]]

        if x[1] in d:
            d[x[1]].append(x[0])
        else:
            d[x[1]] = [x[0]]
    # print(d)
    return len(findPaths2(d))


if __name__ == "__main__":
    print(part1())
    print(part2())
