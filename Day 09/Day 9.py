def neighbors(i, j, a):
    """
    Find the neighbors of a given element in an array
    :param i: input element's row
    :param j: input element's column
    :param a: input array
    :return: list of indices of a[i][j]'s neighbors
    """
    r = len(a)
    c = len(a[0])
    v = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    return [(i+dx, j+dy) for dx, dy in v if 0 <= i+dx < r and 0 <= j+dy < c]


def part1():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if '\n' in lines[i]:
            lines[i] = lines[i][:-1]
    a = list(map(lambda x: list(map(int, list(x))), lines))
    res = 0
    nrows = len(a)
    ncols = len(a[0])
    for i in range(nrows):
        for j in range(ncols):
            c = a[i][j]
            n = neighbors(i, j, a)
            if all(map(lambda x: a[x[0]][x[1]] > c, n)):
                res += c + 1
    return res


def largerNeighbors(i, j, a):
    """
    Find the neighbors of a given element in an array which are smaller than the
    element itself, including the element
    :param i: input element's row
    :param j: input element's column
    :param a: input array
    :return: list containing (i,j) and indices of a[i]ij]'s neighbors which are
             larger than a[i][j]
    """
    n = list(filter(lambda x: a[x[0]][x[1]] > a[i][j] and a[x[0]][x[1]] != 9,
                    neighbors(i, j, a)))
    n.append((i, j))
    return n


def allLargerNeighbors(l, a):
    """
    Given a list of indices (representing the sinks), return a list of valleys
    :param l: list of indices (i, j) representing sinks
    :param a: input array
    :return: list of indices representing all the surrounding elements larger
             than each element in l (i.e. will flow into (i, j))
    """
    t = []
    for x in l:
        for y in largerNeighbors(x[0], x[1], a):
            if y not in t:
                t.append(y)
    # print(t)
    if len(t) == len(l):
        return t
    else:
        return allLargerNeighbors(t, a)


def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if '\n' in lines[i]:
            lines[i] = lines[i][:-1]
    a = list(map(lambda x: list(map(int, list(x))), lines))
    # print(a)
    res = []
    nrows = len(a)
    ncols = len(a[0])
    for i in range(nrows):
        for j in range(ncols):
            c = a[i][j]
            n = neighbors(i, j, a)
            if all(map(lambda x: a[x[0]][x[1]] > c, n)):
                res.append((i, j))
    answers = []
    for i, x in enumerate(res):
        if i < 3:
            answers.append(len(allLargerNeighbors([x], a)))
        else:
            t = len(allLargerNeighbors([x], a))
            if t > min(answers):
                answers.append(t)
                answers.remove(min(answers))
    return answers[0] * answers[1] * answers[2]


if __name__ == "__main__":
    print(part1())
    print(part2())
