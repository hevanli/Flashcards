import random

vocabList = input("What vocab list would you like to use? >> ")

f = open(vocabList, "r").read()
lines = f.splitlines()

english, spanish = [], []
for line in lines:
    comma = line.index(",")
    english.append(line[0:comma])
    spanish.append(line[comma+2:len(line)])

randomBag = random.sample(range(0, len(lines)), len(lines))

for i in randomBag:
    print("The word is " + english[i] + ".")
    answer = input("What is the word in Spanish? >> ")
    while answer != spanish[i]:
        if (answer == "I give up"):
            print("The word was " + spanish[i])
        else:
            answer = input("Incorrect. What is the word in Spanish? >> ")
    print("That's correct!")

print("Good job you completed all the vocabulary!")

    
