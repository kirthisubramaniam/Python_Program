# #Store a message in a variable, then print that message.
x="welcome"
print(x) 

"""
Store a message in a variable, and print that message. 
Then change the value of your variable to a new message, and print the new message

"""
x="Welcome to the bootcamp"
print(x) 

#Store a person’s name in a variable, and print a message to that person. 

y="davina"
print("Hi " + y + "," + x.title() +".")

#Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase

print(y.upper())
print(y.lower())
print(y.title())

"""
Write addition, subtraction, multiplication, 
and division operations that each result in the number 8. 
Be sure to enclose your operations in print statements to see the results.

"""

print(4+4)
print(8-0)
print(2*4)
print(int(16/2))

'''
Store your favorite number in a variable. 
Then, using that variable, create a message that reveals your favorite number. 
Print that message.

'''

a=7
print("Your favourite number is "+ str(a))

'''
Use an f-string to print out a message with a variable.

'''
print(f"Your favourite number is , {a}")

'''
Use multiple variables in one string to print a message.

'''
b=3
print(f"your favorite number is {a} and {b}")

'''
Set three variables, one that says, “Good”, another that says, 
“Day”, and another that says your name. “Add” them together,
 with a space between each word, and store it into another variable. 
Then, print out that variable. 

'''
p="Good"
q="Day"
r="kirthi"
s=p+" "+q+" "+r
print("Hi," + s )
