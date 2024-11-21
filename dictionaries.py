#1.Create a dictionary with three key-value pairs representing a student's information: name, age, and grade. Print each key-value pair on a new line.

student = {
    "name": "Alice",
    "age": 18,
     "grade": "A"
    }
for key, value in student.items():
    print(f"{key}: {value}")

#2.Write a function that takes a dictionary of people's names and their ages, {'Alice': 24, 'Bob': 19, 'Charlie': 30}, and returns a list of names of people who are 21 or older.

def adults(ages):
    adults_list = []
    for name, age in ages.items():
        if age >= 21:
            adults_list.append(name)
    return adults_list

ages = {'Alice': 24, 'Bob': 19, 'Charlie': 30}
adult_names = adults(ages)
print(adult_names)

#3.Given a dictionary representing items in a store with their prices, {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}, write a program that takes a list of items bought, ['apple', 'orange', 'banana', 'banana'], and calculates the total cost.

prices = {'apple': 0.5, 'banana': 0.3, 'orange': 0.7}
items_bought = ['apple', 'orange', 'banana', 'banana']
total_cost = 0
for item in items_bought:
    total_cost += prices[item]
print("Total cost:", total_cost)

#4.Write a program that counts the occurrences of each word in a given sentence. Example: for the sentence "hello world hello," the output should be {'hello': 2, 'world': 1}.
sentence = "hello world hello"
words = sentence.split()
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(word_counts) 
