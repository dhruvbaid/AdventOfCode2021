from functools import reduce

def hexToBin(x: str) -> str:
    """
    Convert single hexadecimal digit to its binary representation
    :param x: hex representation of i (0 <= i <= 15) with or without "0x" prefix
    :return: binary representation of i, length 4
    """
    # Add "0x" prefix to hex representation and convert to binary
    if "0x" in x:
        res = str(bin(int(x, 16)))[2:]
    else:
        res = str(bin(int("0x" + x, 16)))[2:]

    # Pad binary representation to length 4 and return
    res = res.zfill(4)
    return res


# Create a hex-to-binary dictionary
hexDict = {str(hex(x))[2:].upper(): hexToBin(str(hex(x))) for x in range(16)}


def decipherLiteral(bString: str, i: int) -> tuple:
    """
    Decipher a bitstring where index i starts encoding a literal
    :param bString: input bitstring
    :param i: start index
    :return: Tuple (result, rest) where:
             result = ["Literal", version, typeID, decoded number in decimal]
             rest = rest of binary string (not deciphered yet)
    """
    if bString == "" or bString is None or i >= len(bString) - 6:
        return [None]

    # Get version and typeID in decimal
    version = int(bString[i:i+3], 2)
    typeID = int(bString[i+3:i+6], 2)

    # Increment to the actual encoded version of the decimal number
    i += 6

    # String to store number in
    number = ""

    # The number is given as blocks of 5 digits, where the first digit being 0
    # indicates that this is the last block representing that number - so we
    # just loop over the string until we see a block of size 5 starting with a 0
    while True:
        block = bString[i: i+5]
        if block[0] == "1":
            number += block[1:]
            i += 5
        else:
            number += block[1:]
            i += 5
            break
    return ["Literal", version, typeID, int(number, 2)], bString[i:]


def decipherOperator0(bString: str, i: int) -> tuple:
    """
    Decipher a bitstring where index i starts encoding an operator of type 0
    :param bString: input bitstring
    :param i: start index
    :return: Tuple (result, rest) where:
             result = ["Literal", version, typeID, all subpackets (deciphered)]
             rest = rest of binary string (not deciphered yet)
    """
    if bString == "" or bString is None or i >= len(bString) - 6:
        return [], None

    # Get version and typeID in decimal
    version = int(bString[i:i+3], 2)
    typeID = int(bString[i+3:i+6], 2)

    # Using its total bitlength, get this packet's subpackets
    subPacketsLength = int(bString[7:22], 2)
    subPackets = bString[22: 22+subPacketsLength]

    # Increment i to the next packet's start index
    i = 22 + subPacketsLength

    # Decipher the subpackets recursively, return the result
    return ["Operator 0", version, typeID, decipher(subPackets, 0)], bString[i:]


def decipherNum(bString: str, i: int, num: int) -> tuple:
    """
    Decipher a specific number of packets from the given bitstring
    :param bString: input bitstring
    :param i: start index
    :param num: number of packts to decipher
    :return: a tuple containing a list of deciphered packets and the rest of the
             bitstring
    """
    res = []
    if bString == "" or bString is None or i >= len(bString) - 6:
        return res

    # Variable to count number of packets deciphered
    numDeciphered = 0

    # Decipher the appropriate number of packets, append each to res, return
    while len(bString) >= 6 and numDeciphered < num:
        # Get version and typeID in decimal
        version = int(bString[i:i+3], 2)
        typeID = int(bString[i+3:i+6], 2)

        # Decipher using the correct function based on the encoded bitstring
        if typeID == 4:
            curRes, bString = decipherLiteral(bString, i)
            res += curRes
        else:
            if bString[6] == "0":
                curRes, bString = decipherOperator0(bString, i)
                res += curRes
            else:
                curRes, bString = decipherOperator1(bString, i)
                res += curRes
        numDeciphered += 1
        i = 0
    return res, bString


def decipherOperator1(bString: str, i: int) -> tuple:
    """
    Decipher a bitstring where index i starts encoding an operator of type 1
    :param bString: input bitstring
    :param i: start index
    :return: Tuple (result, rest) where:
             result = ["Literal", version, typeID, all subpackets (deciphered)]
             rest = rest of binary string (not deciphered yet)
    """
    if bString == "" or bString is None or i >= len(bString) - 6:
        return [], None

    # Get version and typeID in decimal
    version = int(bString[i:i+3], 2)
    typeID = int(bString[i+3:i+6], 2)

    # Get total number of subpackets
    numSubPackets = int(bString[7:18], 2)

    # Re-align bitstring, return numSubPackets (deciphered) subpackets and rest
    # of bitstring by calling decipherNum
    bString = bString[i+18:]
    res, bString = decipherNum(bString, 0, numSubPackets)
    return ["Operator 1", version, typeID, res], bString


def decipher(bString: str, i: int) -> list:
    """
    Main decipher function
    :param bString: input bitstring
    :param i: start index
    :return: a list containing deciphered packets
    """
    res = []
    if bString == "" or bString is None or i >= len(bString) - 6:
        return res

    # Get version and typeID in decimal
    version = int(bString[i:i+3], 2)
    typeID = int(bString[i+3:i+6], 2)

    # Decipher using the correct function based on the encoded bitstring
    if typeID == 4:
        curRes, bString = decipherLiteral(bString, i)
        res += curRes
    else:
        if bString[6] == "0":
            curRes, bString = decipherOperator0(bString, i)
            res += curRes
        else:
            curRes, bString = decipherOperator1(bString, i)
            res += curRes

    # Recursively decipher rest of bitstring; return result
    res += decipher(bString, 0)
    return res


def sumVersions(a: list) -> int:
    """
    Given a list of deciphered packets, return the sum of their versions,
    computed recursively
    :param a: input list of deciphered packets
    :return: integer representing sum of all packets' and subpackets' versions
    """
    res = 0
    i = 0
    while i < len(a):
        # First element is a list - only happens for outermost packet. Just
        # return the result of the inner packet
        if type(a[i]) == list:
            return sumVersions(a[i])
        # First element is a string - should be "Literal", "Operator 0", or
        # "Operator 1"
        elif type(a[i]) == str:
            # Get version and typeID in decimal
            version = a[i+1]
            typeID = a[i+2]

            # Result - an integer (if packet is a literal) or a list (packet is
            # an operator)
            result = a[i+3]

            # Add version
            res += version

            # Recursively iterate through result if the packet is an operator
            if type(result) == list:
                res += sumVersions(result)
            i += 4
        else:
            raise ValueError("Incorrect type of first element!")
    return res


def evaluate(a: list):
    """
    Evaluate a list of deciphered packets based on operator types and the
    operation it encodes
    :param a: list of deciphered packets
    :return: final result after evaluating operations on all packets recursively
    """
    i = 0
    res = []
    while i < len(a):
        cur = a[i]
        if type(cur) == list:
            res.append(evaluate(cur))
        elif type(cur) == str:
            if "Literal" in cur:
                res.append(a[i + 3])
            elif "Operator" in cur:
                # Get operator type and the subpackets it operates on
                typeID = a[i + 2]
                result = a[i + 3]

                # Evaluate subpackets recursively
                evalResult = evaluate(result)

                # Perform appropriate operation on all evaluated subpackets
                if typeID == 0:
                    # Sum
                    res.append(reduce(lambda x, y: x+y, evalResult))
                elif typeID == 1:
                    # Product
                    res.append(reduce(lambda x, y: x*y, evalResult))
                elif typeID == 2:
                    # Minimum
                    res.append(min(evalResult))
                elif typeID == 3:
                    # Maximum
                    res.append(max(evalResult))
                elif typeID == 5:
                    # Greater than
                    res.append(1 if evalResult[0] > evalResult[1] else 0)
                elif typeID == 6:
                    # Less than
                    res.append(1 if evalResult[0] < evalResult[1] else 0)
                elif typeID == 7:
                    # Equal to
                    res.append(1 if evalResult[0] == evalResult[1] else 0)
                else:
                    raise ValueError("Invalid TypeID")
            else:
                raise ValueError("Invalid first string")
        else:
            raise ValueError("Invalid packet type")
        i += 4
    return res


def part1(bString):
    """
    Sum all versions of all packets from input bitstring
    :param bString: input bitstring
    :return: sum of all versions
    """
    return sumVersions(decipher(bString, 0))


def part2(bString):
    """
    Evaluate all packets
    :param bString: input bitstring
    :return: result of evaluating all packets
    """
    return evaluate(decipher(bString, 0))


if __name__ == "__main__":
    # Parse input
    with open("Input.txt", mode='r') as f:
        lines = f.readlines()
    a = lines[0]
    if '\n' in a:
        a = a[:-1]
    bString = ""
    for x in a:
        if x in hexDict:
            bString += hexDict[x]
        else:
            bString += x

    # Evaluate parts 1 and 2
    print(part1(bString))
    print(part2(bString))

