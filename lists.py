#1.Create a list of 5 fruits and print each fruit on a new line using a for loop.
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)

#2.Write a function that takes a list of numbers and returns a new list with each number squared. Example: [1, 2, 3] should become [1, 4, 9].
def square_list(numbers):
    squared_list = []
    for num in numbers:
        squared_list.append(num**2)
    return squared_list

numbers = [1, 2, 3]
squared_numbers = square_list(numbers)
print(squared_numbers)

#3.Write a Python program that takes two lists, list1 = [1, 2, 3] and list2 = [4, 5, 6], and combines them into a single list, combined = [1, 4, 2, 5, 3, 6].

list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = []
for i in range(len(list1)):
    combined_list.append(list1[i])
    combined_list.append(list2[i])
print(combined_list)

 #4.Given a list of numbers, [3, 1, 4, 1, 5, 9, 2], write a program to find and print the two largest numbers in the list without using the max() function.
numbers = [3, 1, 4, 1, 5, 9, 2]
largest1 = largest2 = numbers[0]
for num in numbers[1:]:
    if num > largest1:
        largest2 = largest1
        largest1 = num
    elif num > largest2:
        largest2 = num
print("The two largest numbers are:", largest1, largest2)
