# -*- coding: utf-8 -*-
"""Final_exam_Kakumani_sai_ethesh.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V2DBpZoSYmG6Rd6DKerYTNdfZ8ChBsO6
"""

#Task 1 for loop to print the square of numbers
for i in range(1, 10):
    square = i * i #calculate the square of the current number (i * i)
    print(f"The square of {i} is {square}")

#Task 2
def check_grades(grades):
    for g in grades: # loop through grades
        print("Pass" if g >= 81 else "Try again")
check_grades([90, 80, 85, 70])

#Task 3
def count_vowels(text):
    text = text.lower() # using this lower fun()the text will be lower case even it's in capital
    vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    for char in text:  #for each character, it checks if the character is a vowel by looking it up in the vowels dictionary.
        if char in vowels:
            vowels[char] += 1 #if it is a vowel, it increments the corresponding count in the vowels dictionary
    print(f"Total vowels: {sum(vowels.values())}")
    for v, count in vowels.items():
        print(f"{v}: {count}")
count_vowels("Bonjour!")

#Task 4
numbers = []
print("Enter numbers one by one. Press Enter to stop:")

while True:
    user_input = input("> ")
    if user_input == "":
        break  # stop if user presses Enter
    numbers.append(float(user_input))  # convert input to number
print("\nCollected numbers:", numbers)
print("Total entries:", len(numbers))
print("Average:", sum(numbers) / len(numbers) if numbers else 0)

#task 5
purchases = [('Alice', 100), ('Bob', 50), ('Alice', 30), ('Bob', 20), ('Clara', 200), ('Clara',300)]

customer_totals = {} # dictionary to store total purchases per customer

for name, amount in purchases: # Calculate totals
    if name in customer_totals:
        customer_totals[name] += amount
    else:
        customer_totals[name] = amount

print("Total purchases per customer:")
for customer, total in customer_totals.items():
    print(f"{customer}: ${total}")

#Task 6

import wbdata

# setting up the parameters
country = "HR"  # croatia's country code
indicator = "SP.POP.TOTL"  # Population indicator
years = ("2010", "2020")

data = wbdata.get_data(indicator, country=country, date=years) # retrieving data

print("Country\tYear\tPopulation")
for entry in data:
    if entry['value'] is not None:
        print(f"Croatia\t{entry['date']}\t{int(float(entry['value'])):,}")