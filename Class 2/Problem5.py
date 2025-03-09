#Problem 5

def greet(name,age):
    print(f"Hello {name}, you are {age} years old!")
    age = int(age);
    print(f"6 years ago, your age is {age-6}")
    
def compare(num1,num2):
    print(f"{num1} is greater than {num2}: {num1 > num2}")
    print(f"{num1} is equal to {num2}: {num1 == num2}")
    print(f"{num1} is less than {num2}: {num1 < num2}")

    
    
name = input("Enter your name: ")
age = input("Enter your age: ")

greet(name,age)
    
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

compare(num1, num2)
