def part1():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    print(lines[0])
    a = list(map(lambda x: x.split(" | ")[1], lines))
    for i in range(len(a)):
        if '\n' in a[i]:
            a[i] = a[i][:-1]
    count = 0
    for x in a:
        tmp = list(map(len, x.split(" ")))
        print(tmp)
        count += tmp.count(2) + tmp.count(4) + tmp.count(3) + tmp.count(7)
    return count

def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    a = list(map(lambda x: x.split(" | "), lines))
    for i in range(len(a)):
        if '\n' in a[i][1]:
            a[i][1] = a[i][1][:-1]
    a = list(map(lambda x: [x[0].split(" "), x[1].split(" ")], a))
    print(a)
    total = 0
    for dis, res in a:
        d = dict()
        for x in dis:
            if len(x) == 2:
                d[1] = x
            if len(x) == 4:
                d[4] = x
            if len(x) == 3:
                d[7] = x
            if len(x) == 7:
                d[8] = x
        for c in d[7]:
            if c not in d[1]:
                UU = [c]
        URDR = d[1]
        ULC = []
        for c in d[4]:
            if c not in URDR:
                ULC.append(c)
        DLDD = []
        for c in d[8]:
            if c not in d[4] and c not in UU:
                DLDD.append(c)
        for x in dis:
            if len(x) == 6:
                # 0,6,9
                if ULC[0] in x and ULC[1] in x:
                    # 6,9
                    sFlag = False
                    for c in URDR:
                        if c not in x:
                            d[6] = x
                            sFlag = True
                    if not sFlag:
                        d[9] = x
                else:
                    # 0
                    d[0] = x
            if len(x) == 5:
                # 2,3,5
                if DLDD[0] in x and DLDD[1] in x:
                    # 2
                    d[2] = x
                else:
                    # 3, 5
                    tFlag = False
                    for c in ULC:
                        if c not in x:
                            d[3] = x
                            tFlag = True
                    if not tFlag:
                        d[5] = x
        c = {d[c]: c for c in d}
        # print(f"{len(c)}")
        myVal = 0
        for i, v in enumerate(res):
            for s in c:
                c1 = (len(list(filter(lambda z: z in s, list(v)))) == len(v))
                c2 = (len(list(filter(lambda z: z in v, list(s)))) == len(s))
                if c1 and c2:
                    myVal += (10 ** (3 - i)) * c[s]
        print(myVal)
        total += myVal
    return total

if __name__ == "__main__":
    # print(part1())
    print(part2())
