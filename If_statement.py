
#if loop to match the string and print output
item=input("Do u want apples or oranges? \n")
if item.lower()=='apples':
    print("You have bought Apples")
elif item.lower()=='oranges':
    print("You have bought Oranges")
else:
    print("Sorry,we have only oranges and apples")

#if statement to check condintion in Int datatype
age=int(input("Please enter the age \n"))
if age<2:
    print("Under 2,The person is baby")
elif age>=2 and age<4:
    print("Between 2 and 4,the person is toddler")
elif age>=4 and age<13:
    print("Between 4 and 13,the person is kid")
elif age>=13 and age<20:
    print("Between 13 and 20,the person is a teenager")
elif age>=20 and age<65:
    print("Between 20 and 65,the person is an adult")
else:
    print("65 and above,the person is an elder")

#Get input from user and then check condition using if condition
inputfruit=input("please enter a fruit name \n")
fruit=inputfruit.title()
favorite_fruits=["Watermelon","Orange","Tomato"]
if fruit in favorite_fruits:
        print(f"Your really like {fruit}")
else:
      print("Its not your favorite")

#If condition in list
usernames=["admin","kirthi_7","jack_3","richard_5","antony_3"]
for name in usernames:
    if name == 'admin':
        print(f"Hello {name}, would you like to see a status report?")
    elif name == 'kirthi_7':
        print(f"Hello {name},thanks for logging in again")
    elif name == 'jack_3':
        print(f"Hello {name},thanks for logging in again")
    elif name == 'richard_5':
        print(f"Hello {name},thanks for logging in again")
    elif name == 'antony_3':
        print(f"hello {name}, thanks for logging in again")

print("Sorry you need to create an account first,contact admin")


#if condition to compare two list
current_users=["kirthi_7","jack_3","richard)_5","antony_3","paula_5"]
new_users=["paula_5","antony_3","dominic_12","mary_23","berni_17"]
for user in new_users:
    if user.lower() in current_users:
        print(f"{user} ,username not available,type new username")
    else :
        print(f"{user},Username is available")





