def part1():
    arr = []
    with open("Day 1 Input.txt", mode = 'r') as f:
        lines = f.readlines()
    # print(len(lines))
    for x in lines:
        arr.append(int(x))
    res = 0
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            res += 1
    return res

def part2():
    arr = []
    with open("Day 1 Input.txt", mode='r') as f:
        lines = f.readlines()
    # print(len(lines))
    for x in lines:
        arr.append(int(x))
    res = 0
    for i in range(len(arr) - 3):
        if arr[i] + arr[i+1] + arr[i+2] < arr[i+1] + arr[i+2] + arr[i+3]:
            res += 1
    return res

if __name__ == "__main__":
    print(part1())
    print(part2())