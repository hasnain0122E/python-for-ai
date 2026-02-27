"""
Functions are reusable blocks of code that 
do specific tasks. Instead of writing the same code
multiple times, you write it once as a function and
call it whenever needed.
"""

def greet():
    print("printing function")
    pass

greet()

def check_weather():
    temperature = 45
    if temperature > 30:
        print("today is too hot!")
    else:
        print("pleasent weather today!")

check_weather()


"""
Parameters: let you pass data into functions.
Instead of hardcoding values, you make functions flexible to 
work with different inputs.
Parameters are passed inside the (here) with the function nme
"""

def user(name, age):
    print(f"Hello, I am {name}, my age is {age}")

user("hasnain", 22)

#setting default values in parameters

def user1(name = "john" , age = 22):
    print(f"Hello, I am {name}, my age is {age}")

user1("hasnain", 23)

#keyword arguments
def calculate_product_price(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = (price + tax) - discount
    print(f"the final price of product is {final_price}")

calculate_product_price(price=250, tax_rate=2.5, discount=20)


"""
Local variables
Variables created inside a function only exist within that function:
"""

"""
Global variables
Variables created outside functions can be accessed anywhere:
"""

"""
The return statement
Use return to send a value back from a function:
to get the output of the function and store in a new variable
"""

def calculate_area(width, height):
    area = width + height
    return area

total_area = calculate_area(200, 500)
print(f"total area: {total_area} sq ft") 