#opening files and print output line by line
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents)

with open('learning_python.txt') as file_object:
    for line in file_object:
        print(line)

with open('learning_python.txt') as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line)

#writing into the files using write command
prompt="Please enter your name\n"
name=input(prompt)

filename = 'guest.txt'

with open(filename,'w') as file_object:
    file_object.write(name)
with open('guest.txt') as file_object:
    contents=file_object.read()
    print(contents)
    
#Usinf if condition to check user input with the files
prompt="Why you like programming?\n"
filename='programming.txt'
while True:
    reason=input(prompt)
    if reason == 'quit':
        break
    else:
        with open(filename,'a') as file_object:
            file_object.write(reason)


with open('programming.txt') as file_object:
    lines=file_object.readlines()

for line in lines:
    print(line)

#Use try and exception method to avoid program error
files_name=['guest','programming','learning_python']
print(files_name)
prompt="Enter a file name from the above list\n"
input=input(prompt)
try:
    name=input+".txt"
    with open(name) as file_objects:
           output=file_objects.read()
           print(output)
    
except FileNotFoundError:
     print("File cannot be found")

try:
   with open("cat.txt") as file_objects:
     content=file_objects.read()
     print(content)
     
   with open("dog.txt") as file_objects:
     content=file_objects.read()
     print(content)

except FileNotFoundError:
     print("File cannot be found")

#Importing json

import json

number=input("What is ypur favorite number\n")

filename='number.json'
with open(filename,'w') as obj:
    json.dump(number,obj)
    print(f"Your favorite number is {number}")

