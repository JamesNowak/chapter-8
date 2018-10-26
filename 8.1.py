# TODO 8.1 Basic string Operation
# 1. Print all the characters from the name variable by accessing one character at a time
print("---------------------------------8.1 question 1 ---------------------------------------")
name = "John Jacob Jingleheimer Schmidt"
for ch in name:
    print(ch)
# 2. Use the index to access and print the capital s in Schmidt from the variable name
print("---------------------------------8.1 question 2 ---------------------------------------")
ch = name[24]
print(ch)
# 3. Use the index with negative numbers to print the letters from the last name "Schmidt" in the
#    name variable
print("---------------------------------8.1 question 3 ---------------------------------------")
print(name[-7], name[-6], name[-5],name[-4], name[-3], name[-2], name[-1])
