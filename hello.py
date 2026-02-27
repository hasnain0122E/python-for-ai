#common data types
#number (number, float), string, boolean(true,false)

#string concatination
first_name = "hasnain"
last_name = "ali"

full_name = first_name + " " + last_name

#string repetition
repetiton = "*" * 20

#length of string
len(repetiton)

#f-string
user_name = "Hasnain"
title = f"hey my name is {user_name}"

#cleaning string
str = "     heyyyyyyyyyyy       "
str.strip()

#finding and replacing
message = "I love Python programming with Python"
print("Python" in message)
print(message.startswith("I"))


#FOR LOOP
#simple loop:
for i in range(0, 20, 4):
    print(i)