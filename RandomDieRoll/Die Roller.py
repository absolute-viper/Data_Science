import random

def WinAmount(dots):
    if dots == 1 or dots == 2:
        return "Loose a dollar"
    elif dots == 3 or dots == 4:
        return "No win no loss"
    elif dots == 5 or dots == 6:
        return "Win a dollar"


if __name__ == '__main__':
    x = random.randint(1, 7)
    print("Dots: {0} ,Outcome: {1}".format(x, WinAmount(x)))
