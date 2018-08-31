import random

PLAYER_SYMBOL = "X"
COMPUTER_SYMBOL = "O"


def eval(s):
    input = str(s)
    if("XXX" in input):
        return "X"
    elif ("OOO" in input):
        return "O"
    elif("-" in input):
        return("-")
    else:
        return("!")


def move(text, position, symbol):
    if(position < 0 or position > 19):
        raise ValueError("Wrong position")
    return text[:position] + symbol + text[position + 1:]


def move_player(text):
    while(1):
        try:
            position = int(input("Enter the position (a number 0-19): "))
            if(position >= 0 and position <= 19):
                if(text[position] != "-"):
                    print("Position taken. Select a different position.\n")
                else:
                    break
            print("Position out of range\n")
        except ValueError:
            print("Position must be a number\n")
    text = move(text, position, PLAYER_SYMBOL)
    print("Actuall state: " + text)
    return text


def move_computer(text):
    while(1):
        position = random.randint(0, 19)
        if(text[position] == "-"):
            break
    text = move(text, position, COMPUTER_SYMBOL)
    print("Actuall state: " + text)
    return text


text = "--------------------"
switcher = {
    str(PLAYER_SYMBOL): "Player won!",
    str(COMPUTER_SYMBOL): "Computer won!",
    "!": "Draw"
}
while(1):
    text = move_player(text)
    if (eval(text) != "-"):
        break
    text = move_computer(text)
    if (eval(text) != "-"):
        break

print(switcher.get(eval(text), "something went wrong"))
