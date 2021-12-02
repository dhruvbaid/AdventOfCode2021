def part1():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    # print(len(lines))
    h = 0
    v = 0
    for x in lines:
        tmp = x.split(" ")
        if tmp[0] == "forward":
            h += int(tmp[1])
        elif tmp[0] == "up":
            v -= int(tmp[1])
        elif tmp[0] == "down":
            v += int(tmp[1])
        else:
            raise ValueError("Invalid input!")
    return h*v

def part2():
    with open("Input.txt", mode = 'r') as f:
        lines = f.readlines()
    # print(len(lines))
    h = 0
    v = 0
    aim = 0
    for x in lines:
        tmp = x.split(" ")
        if tmp[0] == "forward":
            h += int(tmp[1])
            v += aim * int(tmp[1])
        elif tmp[0] == "up":
            aim -= int(tmp[1])
        elif tmp[0] == "down":
            aim += int(tmp[1])
        else:
            raise ValueError("Invalid input!")
    return h*v

if __name__ == "__main__":
    print(part1())
    print(part2())