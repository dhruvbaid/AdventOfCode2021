from functools import reduce


def addDarks(image, n: int, v: str):
    res = []
    t = [v for _ in range(n)]
    for x in image:
        res.append(t + x + t)
    t = [v for _ in range(len(res[0]))]
    newRes = []
    for _ in range(n):
        newRes.append(t)
    newRes += res
    for _ in range(n):
        newRes.append(t)
    return newRes


def getNeighbors(i: int, j: int, img: list):
    dxdy = [(dx, dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]
    res = ""
    for dx, dy in dxdy:
        res += img[i + dx][j + dy]
    return res


def neighborsToInt(s: str):
    return int(reduce(lambda a, b: a + b,
                      list(map(lambda c: "0" if c == "." else "1", list(s)))),
               2)


def enhance(img, enhancement, step: int):
    newImage = []

    if enhancement[0] == ".":
        img = addDarks(img, 3, ".")
    else:
        if step == 0:
            img = addDarks(img, 3, ".")
        else:
            if step % 2 == 0:
                img = addDarks(img, 3, enhancement[-1])
            else:
                img = addDarks(img, 3, enhancement[0])

    numRows = len(img)
    numCols = len(img[0])

    for i in range(1, numRows - 1):
        tmpRow = []
        for j in range(1, numCols - 1):
            tmpRow.append(enhancement[neighborsToInt(getNeighbors(i, j, img))])
        newImage.append(tmpRow)

    newImage = newImage[1:-1]
    for i, r in enumerate(newImage):
        newImage[i] = r[1:-1]

    return newImage


def litCount(img: list) -> int:
    return sum(map(lambda r: r.count("#"), img))


def part1(img, enhancement):
    for step in range(2):
        img = enhance(img, enhancement, step)
    return litCount(img)


def part2(img, enhancement):
    for step in range(50):
        img = enhance(img, enhancement, step)
    return litCount(img)


if __name__ == "__main__":
    # Parse input
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    enhancement = lines[0]
    if '\n' in enhancement:
        enhancement = enhancement[:-1]
    initial = []
    for x in lines[2:]:
        if '\n' in x:
            initial.append(list(x[:-1]))
        else:
            initial.append(list(x))

    # Evaluate parts 1 and 2
    # print(part1(initial, enhancement))
    print(part2(initial, enhancement))

