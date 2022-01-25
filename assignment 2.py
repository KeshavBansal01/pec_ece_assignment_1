print('Question1')

# Input_string has given a value
input_string = 'Python is a case sensitive language'

# Printing the length of input_string.
print("\nPart a ")
print(f"Length of Input String = {len(input_string)}")

# Printing the input_string in reverse order.
print("\nPart b")
print(input_string[::-1])


# slicing and printing the input_string.
print("\nPart c")
sliced_string = input_string[10:26]
print(sliced_string)
print


# replacing and printing.
print("\nPart d")
new_string = input_string.replace("a case sensitive", "object oriented")
print(new_string)


# printing index of "a" from input_string.
print("\nPart e")
print(input_string.index("a"))


# replacing blank white spaces with empty string.
print("\nPart f")
print(input_string.replace(" ", ""))


######################################

print("Question 2")

# putting values of  variables.
name = "Keshav Bansal"
SID = "21105096"
department = "ECE"
CGPA = "9.2"

# Now we are printing the  statements in the given format.
print(f"Hey, {name.title()} here! \nMy SID is {SID} \nI am from {department} and my CGPA is {CGPA}")

######################################


print("Question 3")


a = 56
b = 10

print(" a&b : ", a & b)
print(" a|b : ", a | b)
print(" a^b : ", a ^ b)

# Left shift both a and b with 2 bits.
print("a<<2 : ", a << 2, "\tb<<2 :", b << 2)
# Right shift a with 2 bits and b with 4 bits.
print("a>>2 : ", a >> 2, "\tb>>2 :", b >> 4)


#######################################


print("Question 4")

#  We are taking input of 3 numbers from a user.
x = int(input("Enter 1st number. : "))
y = int(input("Enter 2nd number. : "))
z = int(input("Enter 3rd number. : "))

#finding the highest no.
if x > y:
    if x > z:
        highest_number = x
    else:
        highest_number = z

if y > x:
    if y > z:
        highest_number = y
    else:
        highest_number = z


print(f"Highest no. = {highest_number}")


########################################


print("Question 5")

# taking input string from a user.
input_string = input("Enter input string: ")

if "name" in input_string:
    print("Yes")
else:
    print("No")

##########################################


print("Question 6")

# Taking input as lengths of 3 sides from a user.
x = int(input("Enter 1st length : ")) 
y = int(input("Enter 2nd length : "))
z = int(input("Enter 3rd length : "))

# Checking the  conditions  for a  triangle.
if x+y > z and x+z > y and y+z > x:
    print("Yes")
else:
    print("No")


