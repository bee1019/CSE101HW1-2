# Your name: Bansri Shah
# Your SBU ID: 110335850
# Your NetID: bpshah
#
# Trifid Cipher (Homework 1-2) starter code
# CSE 101, Fall 2018

import string

# DO NOT MODIFY THIS HELPER FUNCTION!!!
def invert(source):
    t = {}
    for k in source:
        t[source[k]] = k
    return t


# COMPLETE THE FUNCTIONS BELOW FOR THIS ASSIGNMENT

def buildEncipheringTable(key):
    key = key.upper()
    key.replace(" ", "")
    available = string.ascii_uppercase + "!"
    available = list(available)

    initial = [1, [], [], []]
    curr_Table = 1

    for i in key:
        if i in available:
            initial[curr_Table].append(i)
            available.remove(i)

        if len(initial[curr_Table]) == 9:
            curr_Table += 1

    for i in available:
        initial[curr_Table].append(i)

        if len(initial[curr_Table]) == 9:
            curr_Table += 1

    my_dict = {}

    for i in range(1, 4):
        for j in range(len(initial[i])):
            firstDigit = i
            letterIndex = j
            secondDigit = (letterIndex // 3) + 1
            thirdDigit = (letterIndex % 3) + 1
            trigram = (firstDigit * 100) + (secondDigit * 10) + thirdDigit

            my_dict[initial[i][j]] = trigram

    return my_dict


def encipher(message, key):
    trigram = buildEncipheringTable(key)
    row_1 = ""
    row_2 = ""
    row_3 = ""

    message = message.upper()
    message = message.replace(" ", "")

    for i in message:
        temp = str(trigram[i])
        row_1 += temp[0]
        row_2 += temp[1]
        row_3 += temp[2]

    new_dict = invert(trigram)
    combined = ""

    while len(row_1) >= 5:
        combined += row_1[:5]
        row_1 = row_1[5:]
        combined += row_2[:5]
        row_2 = row_2[5:]
        combined += row_3[:5]
        row_3 = row_3[5:]

    if len(row_1) != 0:
        combined = combined + row_1 + row_2 + row_3

    enciphered = ""
    code = ""

    for i in combined:
        code += i

        if len(code) == 3:
            enciphered += new_dict[int(code)]
            code = ""

    while len(enciphered) % 5 != 0:
        enciphered += "X"

    t = ""
    joinList = []
    result = ""

    for i in enciphered:
        t += i

        if len(t) == 5:
            joinList.append(t)
            t = ""

    result = " ".join(joinList)
    
    return result
            


# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Testing Part 1
    print('Testing buildEncipheringTable() with key "DRAGON"...')
    table1 = buildEncipheringTable("DRAGON")
    print('The trigram for "R" is:', table1["R"])
    print('The trigram for "I" is:', table1["I"])
    print('The trigram for "Z" is:', table1["Z"])
    print()

    print('Testing buildEncipheringTable() with key "NEPTUNE"...')
    table2 = buildEncipheringTable("NEPTUNE")
    print('The trigram for "B" is:', table2["B"])
    print('The trigram for "J" is:', table2["J"])
    print('The trigram for "V" is:', table2["V"])
    print()

    print('Testing buildEncipheringTable() with key "CHALLENGER"...')
    table3 = buildEncipheringTable("CHALLENGER")
    print('The trigram for "E" is:', table3["E"])
    print('The trigram for "Q" is:', table3["Q"])
    print('The trigram for "T" is:', table3["T"])
    print()

    # Testing Part 2
    print('Calling encipher() with message "TOBEORNOTTOBE" and key "HAMLET":', encipher("TOBEORNOTTOBE", "HAMLET"))
    print()

    print('Calling encipher() with message "SPACETHEFINALFRONTIER" and key "KIRK":', encipher("SPACETHEFINALFRONTIER", "KIRK"))
    print()

    print('Calling encipher() with message "FOUR SCORE AND SEVEN YEARS AGO" and key "LINCOLN":', encipher("FOUR SCORE AND SEVEN YEARS AGO", "LINCOLN"))
    print()

    print('Calling encipher() with message "The Helvetii compelled by the want of everything sent ambassadors to him about a surrender" and key "caesar":', encipher("The Helvetii compelled by the want of everything sent ambassadors to him about a surrender", "caesar"))
    print()

    print('Calling encipher() with message "Alan Turing was a leading participant in the breaking of German ciphers at Bletchley Park" and key "ENIGMA":', encipher("Alan Turing was a leading participant in the breaking of German ciphers at Bletchley Park", "ENIGMA"))
    print()

    print()

