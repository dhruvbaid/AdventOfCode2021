def updateBoard(b, num):
    newBoard = []
    for r in b:
        tmp = []
        for x in r:
            if x[0] == num:
                tmp.append((x[0], 1))
            else:
                tmp.append(x)
        newBoard.append(tmp)
    return newBoard

def checkBoard(b):
    for r in b:
        if len(list(filter(lambda x: x[1] == 0, r))) == 0:
            return True
    for i in range(5):
        c = [r[i] for r in b]
        if len(list(filter(lambda x: x[1] == 0, c))) == 0:
            return True
    return False

def part1():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    calledNumbers = lines[0].split(",")
    allBoards = []
    board = []
    for i in range(1, len(lines)):
        if lines[i] == "\n" or i == len(lines) - 1:
            if board != []:
                allBoards.append(board)
            board = []
        else:
            tmp = lines[i][:-1].split(" ")
            if '' in tmp:
                tmp.remove('')
            tmp = [(x, 0) for x in tmp]
            board.append(tmp)
    # print(allBoards)
    for num in calledNumbers:
        allBoards = list(map(lambda b: updateBoard(b, num), allBoards))
        t = list(filter(checkBoard, allBoards))
        if len(t) == 1:
            winBoard = t[0]
            print(winBoard)
            s = 0
            for r in winBoard:
                for x in r:
                    if x[1] == 0:
                        s += int(x[0])
            print(s)
            print(num)
            print(int(s) * int(num))
            return int(s) * int(num)

def part2():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    calledNumbers = lines[0].split(",")
    allBoards = []
    board = []
    for i in range(1, len(lines)):
        if lines[i] == "\n" or i == len(lines) - 1:
            if board != []:
                allBoards.append(board)
            board = []
        else:
            tmp = lines[i][:-1].split(" ")
            if '' in tmp:
                tmp.remove('')
            tmp = [(x, 0) for x in tmp]
            board.append(tmp)
    # print(allBoards)
    for i, num in enumerate(calledNumbers):
        allBoards = list(map(lambda b: updateBoard(b, num), allBoards))
        t = list(filter(lambda x: not checkBoard(x), allBoards))
        if len(t) == 1:
            winBoard = t[0]
            break

    j = i + 1
    while not (checkBoard(winBoard)):
        winBoard = updateBoard(winBoard, calledNumbers[j])
        j += 1
    j -= 1
    num = calledNumbers[j]
    s = 0
    for r in winBoard:
        for x in r:
            if x[1] == 0:
                s += int(x[0])
    print(f"s = {s}")
    print(f"num = {num}")
    print(int(s) * int(num))
    return int(s) * int(num)

if __name__ == "__main__":
    print(part1())
    print(part2())