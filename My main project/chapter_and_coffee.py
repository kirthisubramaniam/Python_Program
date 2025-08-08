def loc_dic(type):                                  #This method convert the text file to local dictionary
    local_dict=defaultdict(list)
    filename=type
    extension=".txt"
    with open(filename+extension,"r") as file:
        for line in file:
            parts=line.strip().split(":")           #Splitting the lines in to keys and values
            if len(parts)==2:                       #check if the lines was correctly split into exactly two parts
                key,value = parts                   
                local_dict[key]=value               #If so, assign the key-value pair to the dictionary
            else:
                print(f"skipping invalid line:{line.strip()}")
    display_order(type,local_dict)


def display_order(type,local_dict):                  
    key_list=list(local_dict.keys())                #Convert the dictionary key in to a list
    print("\n".join(key_list))                      #Print each item on a new line to show the user what they can choose from
    while True:
        prompt="Select your choice,Enter 'done' once you completed\n"
        choice=input(prompt).lower()
        if choice=='done':
            projectmethod.clear()
            print("Do you like to order in other categories?")
            break
        elif choice not in key_list:
            print("Type a valid entry")
        else:
            order[type].append(choice)              #Add the item to the order dictionary under current category
            print("Added the item in your basket")
            if choice in local_dict:
                process_value(local_dict[choice])   #Calls another fucntion to handle the item's value

def show_order():
    global total_sum
    print("Basket items are")
    for key,value in order.items():
        print(f"{key}:{value}")
    print(f"Total amount {total_sum}")
    
def process_value(cost):
    global total_sum                                # Use global variable
    total_sum += float(cost)                        # Add value to running total
    print(f"Updated Total: {total_sum}")
    
def update_file(type,action):
    filename=type
    extension=".txt"
    access=action
    try:
        if access=="a":
            with open(filename+extension, "a") as file:
                user_input = input("Enter text to add:\n")
                file.write(user_input + "\n")
                print(f"{user_input} added to {filename} list")
        elif access =="r":
            with open(filename+extension, "r") as file:
                lists=file.readlines()
            print(f"the current list are\n{''.join(lists)}")
            user_input = input("Enter text to remove:\n")
            updated_lists=[line for line in lists if line.strip() != user_input]
            with open(filename+extension,"w") as file:
                file.writelines(updated_lists)
            print(f"{user_input} removed from {filename} list")
        else:
            print("Invalid Entry")
    except FileNotFoundError:
        print(f"Error:'{filename+extension}' not found.")
    except Exception as e:
        print(f"unexpected error {e}")

def select_category():
    while True:                                              #Start the infinite loop to prompt, until user choose checkout
        i=input(f"Choose from the below category\nEnter \n\t'b' for books\n\t'd' for drinks\n\t'm' for menu\n\t's' for specials\n\t'checkout' when you are done\n").lower()
        if i=='checkout':
            print("Thanks for Ordering")
            show_order()
            break
        elif i not in category.keys():                       #If the input is not a valid key in category dictionary ,it prints error message
            print("Invalid Entry")
        else:
            projectmethod.clear()
            type=category[i]                                 #Retrives the corresponding value from the category dictionary
            loc_dic(type)

def credential_check():
    code=input("Enter the code:\n")
    try:
        with open("password.txt","r") as file:
            file_code=file.read().splitlines()
        if code in file_code:
            prompt="'b' for Books,'d' for Drinks and 'm' for Menu and 's' for specials : "
            i=input(prompt).lower()
            if i in category:
                type=category[i]
                action=input("Enter 'r' for remove and 'a' for add : ").lower()
                update_file(type,action) 
            else:
                print("Invalid Category")     
        else:
            print("You don't have access to edit")
    except FileNotFoundError:
        print("Error:Password file not found")
    except Exception as e:
        print(f"unexpected error :{e}")

from collections import defaultdict
order=defaultdict(list)

import projectmethod
category={"b":"Books","d":"Drinks","m":"Menus","s":"Specials"}
total_sum=0
projectmethod.clear()
print("Welcome to Chapter and coffee")
prompt="For customer enter '1' and employee enter '2': "
user=input(prompt)
if user=="1":
    print(f"Can I take your order?\n")
    select_category()

elif user=="2":
    credential_check()
    print()
