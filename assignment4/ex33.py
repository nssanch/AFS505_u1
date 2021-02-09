#EX 33 While  Loops

def make_list(i, max, increment):
    numbers = []
    while i < max:
        print(f"At the top is {i}")
        numbers.append(i)

        i += increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")
    return numbers

start = 0
end = 13
count_by = 3
numbers = make_list(start, end, count_by)


print("The numbers: ", end="")
for num in numbers:
    print(num, end=", ")
