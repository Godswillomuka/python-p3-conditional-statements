#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.upper()== "ADMIN" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    pass

def hows_the_weather(temperature):
    # your code here
     if temperature >85 :
         return "It's too dang hot out there!"
     elif 65 >=temperature >=40 :
         return "It's a little chilly out there!"
     elif temperature < 40 :
         return "It's brisk out there!"
     else:
         return "It's perfect out there!"
     pass
    

# def fizzbuzz(num):
#     # your code here
#     if num  %3 == 0 and num %5 == 0:
#         return "fizzBuzz"
#     elif num %3 == 0:
#         return "fizz"
#     elif num %5 == 0:
#         return "Buzz"
#     else:
#         return "num"
#     pass

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
    pass



def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2

    print("Invalid operation!")
    return None


    pass
