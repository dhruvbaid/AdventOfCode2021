d1 = {']': '[',
      ')': '(',
      '}': '{',
      '>': '<'}

score1 = {']': 57,
          ')': 3,
          '}': 1197,
          '>': 25137}


def part1():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    s = 0
    for l in lines:
        a = []
        for x in l:
            if x in d1:
                if a == [] or a.pop() != d1[x]:
                    s += score1[x]
                    break
            else:
                a.append(x)
    return s


d2 = {'[': ']',
      '(': ')',
      '{': '}',
      '<': '>'}

score2 = {']': 2,
          ')': 1,
          '}': 3,
          '>': 4}


def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    s = 0
    totalScores = []
    for l in lines:
        lineFail = False
        a = []
        for x in l:
            if x in d1:
                if a == [] or a.pop() != d1[x]:
                    s += score1[x]
                    lineFail = True
                    break
            else:
                a.append(x)
        if not lineFail:
            t = 0
            for c in a[::-1]:
                if c != '\n':
                    t *= 5
                    t += score2[d2[c]]
            totalScores.append(t)
    totalScores = sorted(totalScores)
    return totalScores[len(totalScores) // 2]


if __name__ == "__main__":
    print(part1())
    print(part2())
