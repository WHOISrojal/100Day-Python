## Dictionaries ##

# Retrieving the items from a dictionary 
dict = {"Name":"Anonymous", "Age":22, "Class":12}
print(dict["Name"])

# Adding new items to dictionary
dict["Address"] = "America"
print(dict)

# Creating empty dictionary
empty = {}
print(empty)

# Wipe an existing dictionary
# dict = {}
# print(dict)

# Edit an item in a dictionary
dict["Age"] = 30
print(dict) 

# Loop through a dictionary
for key in dict:
    # print(key)
    print(dict[key]) 