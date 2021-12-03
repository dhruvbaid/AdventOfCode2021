def part1():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    numPos = len(lines[0]) - 1
    d = dict()
    for i in range(numPos):
        curPos = [l[i] for l in lines]
        if curPos.count("1") > curPos.count("0"):
            d[numPos - 1 - i] = (1, 0)
        else:
            d[numPos - 1 - i] = (0, 1)
    gamma = 0
    epsilon = 0
    for i in d:
        gamma += (2 ** i) * d[i][0]
        epsilon += (2 ** i) * d[i][1]
    return gamma * epsilon

def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    t1 = [x for x in lines]
    t2 = [x for x in lines]
    i = 0
    while len(t1) > 1:
        curPos = [x[i] for x in t1]
        if curPos.count("1") >= curPos.count("0"):
            t1 = list(filter(lambda x: x[i] == "1", t1))
        else:
            t1 = list(filter(lambda x: x[i] == "0", t1))
        i += 1
    i = 0
    while len(t2) > 1:
        curPos = [x[i] for x in t2]
        if curPos.count("1") < curPos.count("0"):
            t2 = list(filter(lambda x: x[i] == "1", t2))
        else:
            t2 = list(filter(lambda x: x[i] == "0", t2))
        i += 1
    o = t1[0][:-1]
    c = t2[0][:-1]
    oR = 0
    cR = 0
    numPos = len(o)
    for i in range(numPos):
        oR += (2 ** (numPos - 1 - i)) * int(o[i])
        cR += (2 ** (numPos - 1 - i)) * int(c[i])
    return oR * cR

if __name__ == "__main__":
    print(part1())
    print(part2())