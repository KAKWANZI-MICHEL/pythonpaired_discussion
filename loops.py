#1.Write a Python program that prints all even numbers between 1 and 20 using a for loop.
for num in range(2, 21, 2):
    print(num)

#2.Use a while loop to ask the user to input a number until they provide a number greater than 10.
num = 0
while num <= 10:
    num = int(input("Enter a number greater than 10: "))

#3.Write a program that prints the multiplication table (from 1 to 10) for numbers from 1 to 5 using nested for loops.
for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end="\t")
    print()

#4.Given a list of integers, [4, 7, 2, 9, 12, 15], write a program using a for loop to find the sum of all odd numbers and print the result.
numbers = [4, 7, 2, 9, 12, 15]
odd_sum = 0
for num in numbers:
    if num % 2 != 0:
        odd_sum += num
print("Sum of odd numbers:", odd_sum)



