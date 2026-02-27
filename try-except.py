"""
TRY EXCEPT BLOCK:
The try block contains code that might fail.
The except block runs if an error happens
"""

try: 
    helpers()
except:
    print("somethig went wrong")


try:
    age = int(input("enter your age"))
    print(f"In 10 yrs, you will be {age + 5} yrs old")
except ValueError:
    print("please enter a number")