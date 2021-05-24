import random

numSides = 20
numRolls = 1_000_000
numWins = 0

print("-------------------")
print("Starting rolls")
print("-------------------")

for i in range(numRolls):
    if random.randint(1, numSides) > random.randint(1, numSides):
        numWins += 1

print(f"{numWins / numRolls * 100}% win rate")
