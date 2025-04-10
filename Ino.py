used1 = False
used2 = False
used3 = False
used4 = False
used5 = False
def changespeech():
    text = input("Insert text to convert: ")
    text.lower()
    subresult = ""
    result100 = ""
    global used1
    global used2
    global used3
    global used4
    global used5
    for letter in text:
        if letter == 'b':
            subresult += 'p'
        elif letter == 'c':
            subresult += 's'
        elif letter == 'd':
            subresult += 'tr'
        elif letter == 'f':
            subresult += 'h'
        elif letter == 'g':
            subresult += 'k'
        elif letter == 'h':
            subresult += 'ä'
        elif letter == 'j':
            subresult += 'sh'
        elif letter == 'k':
            subresult += 'ḱ'
        elif letter == 'l':
            subresult += 'il'
        elif letter == 'o':
            subresult += 'or'
        elif letter == 'p':
            subresult += 'pr'
        elif letter == 'r':
            subresult += 'd'
        elif letter == 's':
            subresult += 'jzs'
        elif letter == 't':
            subresult += 'ch'
        elif letter == 'u':
            subresult += 'ü'
        elif letter == 'v':
            subresult += 'f'
        elif letter == 'x':
            subresult += 'ø'
        elif letter == 'z':
            subresult += 'ẑ'
        elif letter == 'á':
            subresult += 'uh'
        else:
            subresult += letter
    if subresult[-1] == 'r' and subresult [-2] == 't':
        subresult = subresult[:-1]
        subresult = subresult[:-1]
        addvalue1 = "ter"
        result1 = subresult + addvalue1
        used1 = True
    elif subresult[-1] == 'm':
        subresult = subresult[:-1]
        addvalue2 = "im"
        result2 = subresult + addvalue2
        used2 = True
    elif subresult[-1] == 'n':
        subresult = subresult[:-1]
        addvalue3 = "in"
        result3 = subresult + addvalue3
        used3 = True
    elif subresult[-1] == 'w':
        subresult = subresult[:-1]
        addvalue4 = "wuh"
        result4 = subresult + addvalue4
        used4 = True
    elif subresult[-1] == 'y':
        subresult = subresult[:-1]
        addvalue5 = "yih"
        result5 = subresult + addvalue5
        used5 = True
    if used1 == True:
        print(result1)
    elif used2 == True:
        print(result2)
    elif used3 == True:
        print(result3)
    elif used4 == True:
        print(result4)
    elif used5 == True:
        print(result5)
    else:
        print(subresult)
changespeech()