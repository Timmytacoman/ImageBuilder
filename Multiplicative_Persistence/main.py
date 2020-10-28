import time

def getPersistence(num, steps=0):
    # check if single digit
    if len(str(num)) == 1:
        print(f"Number of steps: {steps}")
        return steps
    # multiply each digit in num together
    product = 1
    for i in str(num):
        product *= int(i)
    # increment steps and print new num
    steps += 1
    print(product)
    return getPersistence(product, steps)


# start timer
startTime = time.time()
amountOfNumbersToCalculate = 1e5

# erase file
open("multiplicative_persistence.csv", 'w').close()

# print header
f = open("multiplicative_persistence.csv", 'w')
f.write("Number, Persistence")


# printing and writing to file
for j in range(int(amountOfNumbersToCalculate)):
    print(f"Calculating multiplicative persistence of {j}")
    print(j)
    numSteps = getPersistence(j)
    # f = open("multiplicative_persistence.csv", "a")
    # f.write("\n")
    # f.write(f"{j}, {numSteps}")
    print("\n")

f.close()
endTime = time.time()

# stats about calculations
print(f"Elapsed time: {endTime - startTime} seconds.")
print(
    f"Average time per calculation: {(endTime - startTime) / amountOfNumbersToCalculate} seconds, for {int(amountOfNumbersToCalculate)} calculations.")



