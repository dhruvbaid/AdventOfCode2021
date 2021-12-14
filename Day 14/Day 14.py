def step(pairDict, insertions, lastPair):
    """
    Given a dictionary representing the pairs of letters and their frequencies
    in the input string, a dictionary of insertions representing the original
    pair and the letter to be added in between to make a new triplet, and the
    last pair in the original string, return the new string after a single step
    :param pairDict: {pair of letters: frequency of pair in original string}
    :param insertions: {pair of letters: letter to be added when taking a step}
    :param lastPair: string representing last 2 letters of original string
    :return: letter frequency dictionary, pair frequency dictionary, and last
             pair in new string (after one step)
    """
    # Find out what new last pair will be
    if lastPair in insertions:
        newLastPair = insertions[lastPair] + lastPair[1]
    else:
        newLastPair = lastPair

    # Initialize dictionaries for new string's letter and pair frequencies
    newLetterDict = dict()
    newPairDict = dict()

    # Take a step by adding pairs to the new string and updating corresponding
    # letter frequencies based on number of pairs in the original string and the
    # transformation as dictated by insertions
    # This works by observing that if AB -> C is an insertion, then k AB pairs
    # are converted to k AC and k CB pairs in a single step, and also accounting
    # for the fact that 'C' is double-counted
    for i, pair in enumerate(pairDict):
        l1, l2 = pair[0], pair[1]
        num = pairDict[pair]

        # If this pair will be transformed into a triplet in the new string...
        if pair in insertions:
            newL = insertions[pair]
            newP1 = l1 + newL
            newP2 = newL + l2

            # Add first half of the new triplet into new pairs frequency dict
            if newP1 in newPairDict:
                newPairDict[newP1] += num
            else:
                newPairDict[newP1] = num

            # Add second half of the new triplet into new pairs frequency dict
            if newP2 in newPairDict:
                newPairDict[newP2] += num
            else:
                newPairDict[newP2] = num

            # Add first 2 letters of triplet to new letter frequency dict
            for curL in [l1, newL]:
                if curL in newLetterDict:
                    newLetterDict[curL] += num
                else:
                    newLetterDict[curL] = num
            # Add last letter if the pair is also at the end of original string
            if pair == lastPair:
                if l2 in newLetterDict:
                    newLetterDict[l2] += 1
                else:
                    newLetterDict[l2] = 1

        # If this pair will remain unchanged in the new string...
        else:
            # Add pair into new pairs frequency dict
            if pair in newPairDict:
                newPairDict[pair] += num
            else:
                newPairDict[pair] = num

            # Add first letter of triplet to new letter frequency dict
            for curL in [l1]:
                if curL in newLetterDict:
                    newLetterDict[curL] += num
                else:
                    newLetterDict[curL] = num
            # Add last letter if the pair is also at the end of original string
            if pair == lastPair:
                if l2 in newLetterDict:
                    newLetterDict[l2] += 1
                else:
                    newLetterDict[l2] = 1
    return newLetterDict, newPairDict, newLastPair


def part1():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()

    # Get initial string and last pair
    initial = lines[0][:-1]
    lastPair = initial[-2:]

    # Get all insertions
    insertions = lines[2:]
    for i, x in enumerate(insertions):
        if '\n' in x:
            insertions[i] = x[:-1].split(" -> ")
        else:
            insertions[i] = x.split(" -> ")

    # Obtain letter frequencies, insertions, and pair frequencies dictionaries
    lDict = {x: initial.count(x) for x in set(initial)}
    iDict = {x[0]: x[1] for x in insertions}
    pDict = dict()
    for i in range(len(initial) - 1):
        t = initial[i: i+2]
        if t in pDict:
            pDict[t] += 1
        else:
            pDict[t] = 1

    # Do 10 steps
    for s in range(10):
        lDict, pDict, lastPair = step(pDict, iDict, lastPair)

    # Return difference between frequencies of most and least frequent letter
    l = list(lDict.values())
    return max(l) - min(l)


def part2():
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()

    # Get initial string and last pair
    initial = lines[0][:-1]
    lastPair = initial[-2:]

    # Get all insertions
    insertions = lines[2:]
    for i, x in enumerate(insertions):
        if '\n' in x:
            insertions[i] = x[:-1].split(" -> ")
        else:
            insertions[i] = x.split(" -> ")

    # Obtain letter frequencies, insertions, and pair frequencies dictionaries
    lDict = {x: initial.count(x) for x in set(initial)}
    iDict = {x[0]: x[1] for x in insertions}
    pDict = dict()
    for i in range(len(initial) - 1):
        t = initial[i: i+2]
        if t in pDict:
            pDict[t] += 1
        else:
            pDict[t] = 1

    # Do 10 steps
    for s in range(40):
        lDict, pDict, lastPair = step(pDict, iDict, lastPair)

    # Return difference between frequencies of most and least frequent letter
    l = list(lDict.values())
    return max(l) - min(l)


if __name__ == "__main__":
    print(part1())
    print(part2())
