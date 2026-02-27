#Data Structures in Python
# Lists, Dictionaries, Tuples, Sets

# List is used to store multiple data
# list are indexed starting at 0
# list are mutable - you can change stored data
# list syntax = [] - square brackets

any_var = "hello I am variable"
my_list = ["hasnain", 21, True, any_var]

#access list data
print(my_list[0])
print(my_list[1])

#access last values from list
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])


#access multiple data from list
print(my_list[0:3])
print(my_list[2:])

#changing in list removing adding: append, remove, pop, del, insert
# append: add the new value at the end of the list
# remove add the given value
# pop removes the last values of the list
# insert used to add the value at the position
# del is used to remove the value using index

my_list.append("ali") 
my_list.insert(1, "ali" )

my_list.remove("ali")

my_list.pop()
del my_list[-1]

t = (5,6,7)
print(t[2])

# Dictionaries stores values in key-value pair just like a real dictionary
empty_dic = {}

new_dic = {
    "name" : "hasnain",
    "age" : 22,
    "city" : "karachi",
}

print(new_dic["name"])
new_dic.get("age")

#adding

new_dic["email"] = "hasnain0122@gmail.com"

#remove
del new_dic["email"]
new_dic.pop("age")
new_dic.clear()

#Nested Dictionaries
nested_dic = {
    "hasnain" : {"age" : 22, "marks" : 88, "Grade" : "A"},
    "Ahmed" : {"age" : 20, "marks" : 96, "Grade" : "A+"}
}

print(nested_dic["hasnain"]["age"])
print(nested_dic.get("hasnain", {}).get("marks"))

#tuples are unmutable - cannot be changed - syntax = paranthesis
#set is used to store unique values - syntax = set()

my_tuple = (2, "hello", True)
my_tuple[1]

a , b,c = my_tuple
print(a, b, c)


#set
empty_set = set()

my_set = {22, 22, 22, 90, 65, 90, 100, 21, 21, 88, 24}
unique_tuple =(list(set(my_set)))
unique_tuple[0] = 65
unique_tuple.reverse()


