def FindNum(arr, str, count):
    if str[count - 3] == " ":
        arr.append(int(str[count - 2]))
    else:
        arr.append(int(str[count - 3] + str[count - 2]))


def IsPossible(arr1, arr2, arr3):
    for num1 in arr1:
        if num1 > 12:
            return False
    for num2 in arr2:
        if num2 > 13:
            return False
    for num3 in arr3:
        if num3 > 14:
            return False
    return True


def PossibleSum():
    GameIdCount = 0
    with open('games.txt', 'r') as f:
        for i in range(100):
            possible = True
            game = f.readline()
            red = []
            blue = []
            green = []
            for j in range(len(str(game))):
                if game[j] == "r" and game[j - 1] == " ":
                    FindNum(red, game, j)
                elif game[j] == "g" and game[j - 1] == " ":
                    FindNum(green, game, j)
                elif game[j] == "b" and game[j - 1] == " ":
                    FindNum(blue, game, j)
                elif game[j] == "\n":
                    break
            possible = bool(IsPossible(red, green, blue))
            if possible == True:
                GameIdCount += (i + 1)

        print(GameIdCount)


PossibleSum()