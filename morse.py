dic = {'A': '._',
       'B': '_...',
       'C': '_._.',
       'D': '_..',
       'E': '.',
       'F': '.._.',
       'G': '__.',
       'H': '....',
       'I': '..',
       'J': '.___',
       'K': '_._',
       'L': '._..',
       'M': '__',
       'N': '_.',
       'O': '___',
       'P': '.__.',
       'Q': '__._',
       'R': '._.',
       'S': '...',
       'T': '_',
       'U': '.._',
       'V': '..._',
       'W': '.__',
       'X': '_.._',
       'Y': '_.__',
       'Z': '__..',
       '1': '.____',
       '2': '..___',
       '3': '...__',
       '4': '...._',
       '5': '.....',
       '6': '_....',
       '7': '__...',
       '8': '___..',
       '9': '____.',
       '0': '_____', }


def get_key(val):
    for key, value in dic.items():
        if val == value:
            return key


def to_morse():
    text = input('Enter text in English : ')
    ls = []
    for ch in text:
        if ch.isalpha():
            ls.append(dic[ch.capitalize()] + ' ')
        elif ch.isspace():
            ls.append('/')
        elif ch.isdigit():
            ls.append(dic[ch] + ' ')
        else:
            ls.append(ch)
    print("".join(ls))
    pass


def from_morse():
    text = input('Enter text in Morse : ')
    morse = text.split()
    morse1 = []
    c = 0
    for i in morse:
        if i.startswith('/'):
            morse1.append(' ')
            morse1.append(morse[c][1:])
        else:
            morse1.append(morse[c])
        c += 1

    res = []
    for item in morse1:
        if item.isspace():
            res.append(' ')
        else:
            res.append(get_key(item))
    print("".join(res))
    pass


def continue_prompt():
    ch = input('Do you want to continue (Y/N)? ')[0]
    if ch.capitalize() == 'Y':
        main()
    elif ch.capitalize() == 'N':
        print('Exiting ...')
        exit(0)
    else:
        print('Invalid choice! Try again.')
        continue_prompt()
    pass


def main():
    print('1. To morse\n2. From morse\n3. Exit')
    ch = int(input('Enter choice : '))
    if ch == 1:
        to_morse()
        continue_prompt()
    elif ch == 2:
        from_morse()
        continue_prompt()
    elif ch == 3:
        exit()
    else:
        print('ERR! Invalid Choice, try again.')
        main()


if __name__ == '__main__':
    main()
