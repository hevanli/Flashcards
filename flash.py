# imports
import random
from pathlib import Path

def filesExist(paths: list) -> bool:
    for path in paths:
        if not Path("./" + path + ".txt").is_file():
            return False
    return True

def main():
    # initializing program
    vocabLists = input("What vocab list would you like to use? >> ").split(",")
    while not filesExist(vocabLists):
        vocabLists = input("Invalid file(s), try again >> ").split(",")
    side = input("Spanish to English, or English to Spanish? (a or b) >> ")
    while side not in ["a", "b"]:
        side = input("Please choose either <a> or <b> >> ")

    allLines = []
    for vocabList in vocabLists:
        f = open(vocabList + ".txt", "r").read()
        allLines.extend(f.splitlines())
    
    l1, l2 = [], []
    for line in allLines:
        comma = line.index(",")
        if side == "a":
            l1.append(line[0:comma])
            l2.append(line[comma+2:len(line)])
        else:
            l2.append(line[0:comma])
            l1.append(line[comma+2:len(line)])
    
    randomBag = random.sample(range(0, len(allLines)), len(allLines))
    
    mistakes, giveUps = 0, 0
    # flash carding
    for i in randomBag:
        print("The word is " + l1[i] + ".")
        answer = input("What is the translation? >> ")
    
        giveUp = False
    
        while answer != l2[i]:
            if (answer == "I give up"):
                print("The word was " + l2[i])
                giveUps += 1
                giveUp = True
                break
            else:
                mistakes += 1
                answer = input("Incorrect. What is the translation? >> ")
        if not giveUp:
            print("That's correct!")
    
    print("Good job you completed all the vocabulary!")
    print("You made", mistakes, "mistakes")
    print("And you gave up", giveUps, "times")
    
if __name__ == "__main__":
    main()
