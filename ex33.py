'''i = 0
numbers = []

for i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)'''


def while_function(i, n, numbers):
    if (i < n):
        print("At the top i is %d") %i
        numbers.append(i)

        i += input()
        print("Numbers now: "), numbers
        print("At the bottom i is %d") %i
        while_function(i, n, numbers)
    return numbers

numbers = while_function(0,6,[])
for num in numbers:
    print(num)
