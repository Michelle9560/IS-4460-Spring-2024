# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11ZxdhEU2c9XdrGUGMBTxqM8ASiVKlCm2
"""

print(f"is 20 gt 10? {20 > 10}")

print(f"is 5 lt 2? {5 > 2}")

print(f"a: {19 > 10}")

print(f"b: {4 == 9}")

print(f"c: {1 == 0}")

print(f"d: {7 == 7}")

print("one is equal to 2:",int(1==2))

print("one is equal to 1:",int(1==1))

myname = "Michelle"
myage = 20

print(f"a: {77}") #numeric literal

print(f"b: {'Hello'}") #string literal

print(f"c: {False}") #constant literal

print(f"d: {myname}") #string variable

print(f"e: {myage}") #numeric variable

print((2 - 5 + 4),(4 - 7 + 10))

print((2 * 2 + 5),(4 * 7 + 9)) #Follows the same precedence in math operations

print(f" is 'michelle' == 'michelle ? {'michelle' == 'michelle'} ") #relational operators

print(f"is 'michael' == 'michelle'? {'michael' == 'michelle'}") #relational operators

# Equality comparison
a = 7
b = 5
result = a == b
print(f"Is a equal to b? {result}")

a = 'hello'
b = 'hello'
result = a == b
print(f"Is a equal to b? {result}")

a = 13
b = 7
result = a == b
print(f"Is a equal to b? {result}")

my_name = "michelle"

print("assignment: ",my_name)

print("equality: ",my_name == "michelle") #equalty operator

print("comparison:", "aa" < "b") #comparison operator

print("comparison:",7 < 10)

print("comparison:",8 >= 10)

print("comparison:", 1 <= 10)

a = 5
b = 7

print(f"comparison: {a} is greater than {b}" if a > b else "")

print(f"comparison: {a} is less than {b}" if a < b else "")

print(f"comparison: {a} is greater than or equal to {b}" if a >= b else "")

print(f"comparison: {a} is less than or equal to {b}" if a <= b else "")

bank_balance = 80
savings = 100
if bank_balance < 100: #if statement
    money = 1000
    bank_balance += money
elif bank_balance > 200: #elif
    savings += 100
    bank_balance -= 100
else:
  print("balance is less than or equal to 100.") #else statement

#can print these to see results
print(bank_balance)
print(savings)

#ternary operator
fuel = 2
print("Fill tank now" if fuel <= 2 else "There's not enough fuel")

#While Loop
fuel = 7
while fuel > 1:
  #keep driving
  print("There's enough fuel")
  fuel -= 1

#For Loop
books = ['harry potter', 'youve reached sam', 'the memory police']
for book in books:
    print(f"book: {book}")

for i in range(5):
    print(f'i: {i}')

#For Loop

#example of using break
for count in range(10):
    print(f"{count} times 13 is {count * 13}")
    if count == 7:
      break

#example of using 'continue'
for count in range (10):
  if count == 7:
    continue #skips 7 times 12 but continues with the rest of the mutiplications
  print(f"{count} times 13 is {count * 13}")