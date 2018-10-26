# TODO 8.3 Testing, Searching, and manipulating strings
print("---------------------------------8.3 question 1 ---------------------------------------")
# 1. Test to see if the string "Jacob" is in name, print the result
text = "I cant believe that Jacob did that!"
if "Jacob" in text:
    print("Jacob was found.")
else:
    print("Jacob was not found.")
print("---------------------------------8.3 question 2 ---------------------------------------")
# 2. Test to see if the string "Michael" is in name, print the result
text_2 = "When is Michel going to take us to the store?"
if "Micheal" in text:
    print("Michael was found.")
else:
    print("Michael was not found.")
print("---------------------------------8.3 question 3 ---------------------------------------")
# 3. Test to see if name is a number, print the result
name = "Sarah"
if name.isdigit():
    print('This is a number.')
else:
    print('This is not a number.')
print("---------------------------------8.3 question 4 ---------------------------------------")
# 4. Test to see if number is a number, print the result
number = "42"
if number.isdigit():
    print('This is a number.')
else:
    print('This is not a number.')

print("---------------------------------8.3 question 5 ---------------------------------------")
# 5. Search for "J" in name, replace with "j" (lower case), print the result - note either assign this to a variable or just print
name_2 = "James"
print(name_2.replace("J","j"))

print("---------------------------------8.3 question 6 ---------------------------------------")
# 6. Split the string name into the variable name_list, replace the ""
name_list = name[:], name_2[:]
print(name_list)
