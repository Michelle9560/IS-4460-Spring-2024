# This is a comment
print("Hello World!")
print("Hello Class!")

# This is an object type string
print('Enhypen')

# This is a number. Technically a float
print(3.8)

# Performing addition
print(7+7)

a = 7
b = 3

print(a+b)

# Demonstrating variable case sensitivity
A = 7
a = 3
print(a)
print(A)

# Showing how to use type()
A = 9
a = 5
print(type(A))

user_name = 'Enhypen'
gpa = 3.8

print(user_name)
print(gpa)

print(type(4.0))

# Definition of the add_numbers function
def add_numbers(a,b):
    print(a+b)
    print(b)

add_numbers(b=5,a=10)

def add_number(a,b):
    output = a + b
    return output

# Calling the function with positional arguments
print(add_number(5,10)) # This should return the sum of 5 and 10

# Calling the function with named arguments
print(add_numbers(b=5,a=10)) # This will print the sum and the value of b

name = "Jaime"

def say_hello():
    name = "John"
    print(name)

say_hello()

def say_hello():
    name = "John"
    return f"hello {name}"

print(say_hello())

print(name)

print("My name is " + user_name + " not Inigo")
print(f"My name is {user_name} not Inigo")

number = 2468 * 1359
print(str(number)[1:3]) # Use str() to convert the number to a string and slice to get specific character