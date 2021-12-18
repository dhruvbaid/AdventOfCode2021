def step(x, y, xVel, yVel):
    x += xVel
    y += yVel

    # Drag
    if xVel > 0:
        xVel -= 1
    elif xVel < 0:
        xVel += 1
    else:
        pass

    # Gravity
    yVel -= 1

    # Final position and velocity
    return x, y, xVel, yVel


def isValid(xVel, yVel, xMin, xMax, yMin, yMax):
    x, y, xVel, yVel = 0, 0, xVel, yVel
    while True:
        x, y, xVel, yVel = step(x, y, xVel, yVel)
        if xMin <= x <= xMax and yMin <= y <= yMax:
            return True
        if (x < xMin and xVel <= 0) or (x > xMax and xVel >= 0):
            return False
        if y < yMin and yVel <= 0:
            return False


def maxHeight(xVel, yVel, xMin, xMax, yMin, yMax):
    if yVel <= 0:
        return 0
    x, y, xVel, yVel = 0, 0, xVel, yVel
    yMax = 0
    while True:
        x, y, xVel, yVel = step(x, y, xVel, yVel)
        if y > yMax:
            yMax = y
        if yVel <= 0:
            break
    return yMax


def part1(xMin, xMax, yMin, yMax):
    validVels = []
    for xVel in range(-250, 250):
        for yVel in range(-250, 250):
            if isValid(xVel, yVel, xMin, xMax, yMin, yMax):
                validVels.append((xVel, yVel))
    return max(list(map(lambda x: maxHeight(x[0], x[1], xMin, xMax, yMin, yMax),
                        validVels)))


def part2(xMin, xMax, yMin, yMax):
    validVels = []
    for xVel in range(-250, 250):
        for yVel in range(-250, 250):
            if isValid(xVel, yVel, xMin, xMax, yMin, yMax):
                validVels.append((xVel, yVel))
    return len(set(validVels))


if __name__ == "__main__":
    # Parse input
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    lines = lines[0][13:].split(", ")
    lines[0] = lines[0].split("..")
    lines[1] = lines[1].split("..")
    lines[0][0] = lines[0][0][2:]
    lines[1][0] = lines[1][0][2:]
    xMin, xMax = list(map(int, lines[0]))
    yMin, yMax = list(map(int, lines[1]))

    # print(f"[{xMin}, {xMax}], [{yMin}, {yMax}]")

    # Evaluate parts 1 and 2
    print(part1(xMin, xMax, yMin, yMax))
    print(part2(xMin, xMax, yMin, yMax))

