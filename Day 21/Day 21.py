from collections import deque

def dieMod(d):
    while d >= 101:
        d -= 100
    return d


def posMod(p):
    while p >= 11:
        p -= 10
    return p


def part1(p1Pos, p2Pos):
    p1Score, p2Score = 0, 0
    turn = 1
    dStart = 1
    dRoll = 0
    while p1Score < 1000 and p2Score < 1000:
        dPos = dieMod(dStart) + dieMod(dStart + 1) + dieMod(dStart + 2)
        dRoll += 3
        if turn == 1:
            p1Pos = posMod(p1Pos + dPos)
            p1Score += p1Pos
            turn = 2
        else:
            p2Pos = posMod(p2Pos + dPos)
            p2Score += p2Pos
            turn = 1
        dStart = dieMod(dStart + 3)
    return min(p1Score, p2Score) * dRoll


dieRolls = {3: 1,
            4: 3,
            5: 6,
            6: 7,
            7: 6,
            8: 3,
            9: 1}

def part2(p1Pos, p2Pos):
    l = deque([(p1Pos, p2Pos, 0, 0, 1, 1)])
    f = {1: 0, 2: 0}
    t = 0
    while len(l) != 0:
        p1Pos, p2Pos, p1Score, p2Score, turn, numUniverses = l.popleft()
        if p1Score >= 21 or p2Score >= 21:
            if p1Score > p2Score:
                f[1] += numUniverses
            else:
                f[2] += numUniverses
            print(f[1] + f[2] - 444356092776315 - 341960390180808)
        else:
            for d in dieRolls:
                if turn == 1:
                    newPos = posMod(p1Pos + d)
                    l.append((newPos,
                              p2Pos,
                              p1Score + newPos,
                              p2Score,
                              2,
                              numUniverses * dieRolls[d]))
                else:
                    newPos = posMod(p2Pos + d)
                    l.append((p1Pos,
                              newPos,
                              p1Score,
                              p2Score + newPos,
                              1,
                              numUniverses * dieRolls[d]))
    print("Done")
    return 1


if __name__ == "__main__":
    with open("Input2.txt", mode='r') as f:
        lines = f.readlines()
    p1, p2 = lines
    if '\n' in p1:
        p1 = p1[:-1]
    if '\n' in p2:
        p2 = p2[:-1]
    p1 = int(p1[len("Player 1 starting position: "):])
    p2 = int(p2[len("Player 2 starting position: "):])
    # Evaluate parts 1 and 2
    # print(part1(p1, p2))
    print(part2(p1, p2))

