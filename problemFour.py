# Haroon Nasir
# 08/09/2025

# For numbers in a range starting from 1 to 50, program prints if the number is divisible by 3, 5, or both. If none then prints number

# for loop that iterates from to to 50
for i in range(1, 51):  
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)