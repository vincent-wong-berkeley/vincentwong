# --- Variables and Data Types --- 

a = 10 
print(a)
print(type(a))
# a is an interger. whole numbers

b = 1.5
print (b)
print(type(b))
# b is a float. fractional number or number with decimals

c = 3j
print (c)
print(type(c))
# c is a string. words or text

d = "hello"
print (d)
print(type(d))
# d is a string. words or text

e = [1, 2, 3]
print (e)
print(type(e))
# e is a list.

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print(type(f))
# f is a dictionary. Stores information in unique key-value pairs

g = (1, 2)
print (g)
print (type(g))
# g is a tuple. assigns a tuple containing the integer values (1, 2) to the variable (g)

h = ["apple", "banana", "strawberry"]
print (h)
print (type(h))
# h is a list.

i = True
print (i)
print (type(i))
# i is a bool.

j = None
print (j)
print (type(j))
# j is a NonType.

k = [True, "blue", 12]
print(k)
print(type (k))
# k is a list.

l = str(14)
print(l)
print(type (l))
# k is a string

m = 1e4
print(m)
print(type(m))
# k is a float

# Questions
# 1. 9 different data types
# 2. int, float, complex, str, list, dict, tuple, bool, NoneType
# 3. c, d, k are strings. e, k are lists. 
# 4. The data type of 1 was str. Strings include more than just whole numbers, including characters. 
# 5. Complex. 

n = 1+2j 
print(n)
print(type(n))
# n is a complex. Represents complex numbers

# 3.2 Booleans
print(10 > 9) # True, 10 > 9.
print(10 == 9) # False. 10 does not equal 9
print(10 <= 9) # False. 10 is not less than or equal 9.
print(bool("abc")) # True. Bool has contents, meaning it is true. 
print(bool(123)) # True
print(bool(["apple", "cherry", "banana"])) # True
print(bool(True)) # True
print(bool(False)) # False
print(bool(0)) #False
print(bool("")) #False
print(bool(" ")) #True
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False
print(bool(True and False)) # False
print(bool(True and True)) # True
print(bool(False and False)) # False
print(bool(True or False)) # True
print(bool(True or True)) # True
print(bool(False or False)) #False
print(bool(not(False))) # True
print(bool(not(True))) # False

# 1. True if bool has contents within. False if not. False is there is no text inside. 
# 2. I was surpsied bool(" ") was True. I thought space would mean it would be false. 
# 3. 
print(bool(0.0)) # False. A float returns as false.
# 4
print(bool(".")) # True. A period counts as a character

# 3.3 Operators
print(10 + 5) # 15 Addition
print(10 - 5) # 5 Subtraction
print(2 * 4) # 8 Multiplication
print(6/3) # 2 Division
print(5 % 2) # 1 Shows remainder of 5/2
print(3 ** 2) # 9 Square root/exponent
print(15//2) # 7 Performs division, but rounds down to nearest whole interger

print( 5 == 2) # False, 5 does not = 2.
print(10 != 10) # False, != means not equal to.
print (2 < 5) # True. 2 is less than 5
print (12>5) # 12 is greater than 5
print (5 <= 16) # True, 5 is less than or equal to 16
print ( 1>= 10) # False, 1 is not greater than or equal to 10

x = 5
x += 5
print(x) # 10

x -= 4
print(x) # 6

x *= 3
print(x) # 18

x = 10
y = 10
# The operator, and, requires two values to be considered simutaniously for it to continue.
if y and x == 10:
    print("x and y = 10")
# The operator, or, means one or another value needs to be considered
if x or y == 10:
    print("x or y = 10")
# The operator, not, requires the a value to NOT be true
condition = not (x>5)

# 1.  / returns a pricide result while // rounds to the nearest interger. 
# 2. % returns the remainder of a division while // returns the actual division
# 3. Use % when calculating the remainder when dividing two numbers
13 % 3
# 4. Assigns a value to a variable. 


# 3.4 Strings
my_string = "hello"

print(my_string)
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])
print(my_string[-1])
print(my_string[1:3])
print(my_string[0:5:2])
print(len(my_string))
print(my_string + "goodbye")
print(my_string*7)

#Slicing: Allows for a new sequence containing the original elements without modifying the original. 
name = "Oski"
print("Hello, my name is", name)
name = "Oski"
print(f"Hello, my name is {name}")
#f strings allow for concise labling + listing for variables. 


# 3.5 Terminal Commands
#cd
# cd: Change directories. Move from one folder to another
# Example: cd Downloads

#ls
# ls: Lists directory 
# ls

# ls -a
# Lists all directory contents (including hidden)

# mkdir
# Makes a new directory/creates a new folder
# mkdir new_folder

# cat
# Concentrates and displays file contents. Displays contents of a file.
# cat my_folder.txt

# pwd
# Print working directory. See which folder you're in. 
# pwd

# cd ..
# Moves up one directory. Moves to a parent directory
# cd .. 

# cd .
# References to cirrent folder. Doesn't move like cd ..

# cd ~
# Moves to home directory/main user folder
# cd ~

# cp
# Makes a copy of a file/folder and puts it into a new location
# cp my_file.txt Documents / (this moves my_file.txt to documents)

# mv
# Moves/renames files. Move a file or folder from one location to another. Also can rename file 
# mv my_file.txt new_file.txt 

# rm
#Removes files/directories. Does not send to trash, deletes permanently.
# rm old_file.txt

# clear
# clears terminal page

# grep
# Searches for pattern in files. Find lines that follow a pattern
# grep "error" log.txt / (This finds all lines with "error" in log.txt)

# less
# Shows fewer options than cat.  Useful for large text files.
# Less long_text.txt

# Top 
# Shows what is using the most resources on your computer. 
# Useful for monitoring system performance

# man
# Short for "manual". Helpful when you don't know how to use a command.
# man ls (opens a manual for ls)



# ls does not show hidden files. ls -a shows all files, including hidden ones

# A hidden file begins with a period. Hidden to prevent accidental modification/clean system.

# -1 
# a detailed list of files and directories. 
# ls -1

# -h 
# A flag that makes the output "human-readable"
# Useful for commands that report files sizes

# -i
# A flag that enables "interactive" mode. Will ask for confirmation before deleting files.
# rm -i file_to_delete.txt (Will prompt confirmation before deleting)