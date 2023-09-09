# listAndDictionary.py
# dH
# 8/27/23
# updated: 9/8/23
#
# Lists[] and Dicts{}
#
# A list of numbers
#
# Demo program for Python Program 03 - Lists and Dictionaries

from random import randrange
from collections import Counter


my_list_of_nums = [11, 5, 33, 74, 55]
print(my_list_of_nums)
print("my_list_of_nums[3] is: " + str(my_list_of_nums[3]))
print("my_list_of_nums[] is: " + str(my_list_of_nums))
# change an element in the list
my_list_of_nums[2] = 745312
print("my_list_of_nums[] is: " + str(my_list_of_nums))
# Loop thru the list with a for-in loop()
for i in my_list_of_nums:
    print(i)
print("*********")
print("")
for num in my_list_of_nums:
    print(num)

# TODO: Add 1000 random numbers to your list with a while loop
new_num = 0

# the while loop control variable is named i
# i is initialized to the value of 1000
i = 1000
# the test condition for the while loop is i > 0
while i > 0:
    new_num = randrange(10)
    # add to my_list_of_nums
    my_list_of_nums.append(new_num)
  #  print("random number, " + str(new_num) + " added to list!")
    i = i - 1
print("\n\n the list is now...")
print(my_list_of_nums)
# use a for/in list to display the numbers
# for i in my_list_of_nums:
#   print(i)

# use a dictionary to count the number of similar numbers in our list
# create a dictionary
the_numbers = {}
# use a for/in list to create the numbers
for i in my_list_of_nums:
    if the_numbers.get(i) is None:
       # print("Key not found, creating one now...")
        # Create a new key with an initial value of 1
        the_numbers[i] = 1
    else:
        # print("Key found, incrementing the value of the key now!")
        # Add 1 to the value of the char found
        the_numbers[i] = the_numbers[i] + 1
# output the dictionary
print("\n\n")
for k, v in the_numbers.items():
    print(str(k) + ": " + str(v))


print("*********")
print("")
my_dict_of_chars = {}
print("my_dict_of_chars is a " + str(type(my_dict_of_chars)))
my_dict_of_chars["a"] = 0
my_dict_of_chars["b"] = 8
print(my_dict_of_chars)
my_str = "The quick brown fox jumped over the lazy dog. and The lazy dog bowed to the regal fox."
print(my_str)

for i in my_str:
    print(i)
    # the first char is 'T', so we need a key named "T"
    # check if "T" is none or not.
    if my_dict_of_chars.get(i) == None:
        print("Key not found, creating one now...")
        # Create a new key with an initial value of 1
        my_dict_of_chars[i] = 1
    else:
        print("Key found, incrementing the value of the key now!")
        # Add 1 to the value of the char found
        my_dict_of_chars[i] = my_dict_of_chars[i] + 1

# print the dictionary
print("my_dict_of_chars is a " + str((my_dict_of_chars)))
# In this for,in loop, the K loop control variable represents the key and the V represents the value of the key.
# Your output should show the number of specific characters in my_str
for k, v in my_dict_of_chars.items():
    print(k + ": " + str(v))

# Sort the dictionary by ASCII value of the chars that are the keys
# in other words... Sort the dictionary by keys in ascending (alphabetical) order.
print(sorted(my_dict_of_chars))
print("")
for k, v in sorted(my_dict_of_chars.items()):
    print(k + ": " + str(v))
print("")
# Sort the dictionary by value.
for i in sorted(my_dict_of_chars, key=my_dict_of_chars.get, reverse=True):
    print(i + ": ",  my_dict_of_chars[i])


# Use Counter
print(" Now try this with a counter...")
my_counter = Counter(my_str)
print(my_counter)
print(my_counter.most_common())
print(my_counter.values())
print("getting the es...")
print(my_counter.get('e'))








