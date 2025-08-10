# Haroon Nasir
# 08/09/2025

# Creates a list of numbers, and asks user if they want solution to part a or b, and gives their respected output

# initializes list of numbers, and saves input in variable
numList = [12, 10, 32, 3, 66, 17, 42, 99, 20]
part = input("What part of problem 2 do you want to see? (a or b)")

# Shows solution for the problem requested
if part == "a" or part == "A":
    for num in numList:
        print(num)

elif part == "b" or part == "B":
    for num in numList:
        numS = num * num
        print(f"number: {num}, number squared: {numS}")