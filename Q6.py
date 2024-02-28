# Here I created a list that is only 1, 2, 3 and then added number 4 into it and changed 2 for 15
numbers = [1,2,3]
print(numbers)
numbers.append(4)
numbers[1] = 15
print(numbers)

# If we try a to modify a string we get and error
string = ("Hello World")
string[1] = "q"