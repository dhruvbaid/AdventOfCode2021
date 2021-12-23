from math import floor, ceil


def explode(s: str):
    i = 0
    level = 0
    while i < len(s):
        if s[i] == "[":
            level += 1
        if s[i] == "]":
            level -= 1
        if level > 4 and s[i] == "[":
            while "[" in s[i+1:] and s[i+1:].index("[") < s[i+1:].index("]"):
                i += 1
            j = i
            toExplodeLeft = i
            while s[j] != "]":
                j += 1
            toExplodeRight = j + 1
            toExplode = s[toExplodeLeft:toExplodeRight]
            lVal, rVal = list(map(int, toExplode[1:-1].split(",")))
            while i >= 0 and s[i] in ["[", "]", ","]:
                i -= 1
            if i != -1:
                eIndexL = i + 1
                while i >= 0 and s[i] not in ["[", "]", ","]:
                    i -= 1
                sIndexL = i + 1
                lValNew = lVal + int(s[sIndexL:eIndexL])
            else:
                # sIndexL, eIndexL = 0, 0
                lValNew = None

            while j < len(s) and s[j] in ["[", "]", ","]:
                j += 1
            if j != len(s):
                sIndexR = j
                while j < len(s) and s[j] not in ["[", "]", ","]:
                    j += 1
                eIndexR = j
                rValNew = rVal + int(s[sIndexR:eIndexR])
            else:
                # sIndexR, eIndexR = 0, 0
                rValNew = None

            if lValNew is None and rValNew is None:
                return s[:toExplodeLeft] + "0" + s[toExplodeRight:]
            elif lValNew is None and rValNew is not None:
                return s[:toExplodeLeft] + "0" + s[toExplodeRight:sIndexR] + str(rValNew) + s[eIndexR:]
            elif lValNew is not None and rValNew is None:
                return s[:sIndexL] + str(lValNew) + s[eIndexL:toExplodeLeft] + "0" + s[toExplodeRight:]
            else:
                return s[:sIndexL] + str(lValNew) + s[eIndexL:toExplodeLeft] + "0" + s[toExplodeRight:sIndexR] + str(rValNew) + s[eIndexR:]
        i += 1
    return s


def split(s: str):
    i = 0
    while i < len(s):
        if s[i] not in ["[", "]", ","]:
            sIndex = i
            while i < len(s) and s[i] not in ["[", "]", ","]:
                i += 1
            eIndex = i
            num = int(s[sIndex: eIndex])
            if num >= 10:
                nMin = int(floor(num/2))
                nMax = int(ceil(num/2))
                if eIndex < len(s):
                    return s[:sIndex] + f"[{nMin},{nMax}]" + s[eIndex:]
                else:
                    return s[:sIndex] + f"[{nMin},{nMax}]"
        i += 1
    return s


def reduce(s: str):
    while s != explode(s):
        s = explode(s)
    return s if s == split(s) else reduce(split(s))


def add(s1: str, s2: str):
    return f"[{s1},{s2}]"


def magnitude(s: str):
    if "[" not in s and "]" not in s and "," not in s:
        return int(s)
    elif s.count("[") == 1 and s.count("]") == 1:
        l, r = list(map(int, s[1:-1].split(",")))
        return (3 * l) + (2 * r)
    else:
        s = s[1:-1]
        i = 0
        count = 0
        while i < len(s):
            if s[i] == "[":
                count += 1
            if s[i] == "]":
                count -= 1

            if count == 0 and s[i] == ",":
                lNum = s[:i]
                rNum = s[i+1:]
                return (3 * magnitude(lNum)) + (2 * magnitude(rNum))

            i += 1


def part1(numberList):
    res = numberList[0]
    for i in range(1, len(numberList)):
        res = reduce(add(res, numberList[i]))
    return magnitude(res)


def part2(numberList):
    maxMag = magnitude(reduce(add(numberList[0], numberList[1])))
    for i in range(len(numberList)):
        for j in range(len(numberList)):
            if j != i:
                t = magnitude(reduce(add(numberList[i], numberList[j])))
                if t > maxMag:
                    maxMag = t
    return maxMag


if __name__ == "__main__":
    # Parse input
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    lines = list(map(lambda x: x[:-1] if '\n' in x else x, lines))

    # Evaluate parts 1 and 2
    print(part1(lines))
    print(part2(lines))

