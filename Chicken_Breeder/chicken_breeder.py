import os
import time
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

record=["Mani","Selvi","chikku","Vadivu","Amulu","Ambi"]

def main_menu():
    while True:
        time.sleep(3)
        clear()
        print("Press 0 to exit th app")
        print("Press 1 to List of Chicken Record")
        print("Press 2 to Create New Chicken Record")
        print("Press 3 to Update the existing Chicken Record")
        print("Press 4 to Delete a Chicken Record")

        value=input("Enter your option \n")
        if value=="0":
            print("Thanks for your time,Goodbye \n")
            break
        elif value=="1":
            show_record()
        elif value=="2":
            add_record()
        elif value=="3":
            update_record()
        elif value=="4":
            delete_record()
        else:
            print("Input Valid entry")

def show_record():
    print("The current chicken lists are")
    for index, name in enumerate(record):
        print(f"{index}: {name}")


def add_record():
    print("Enter the name to add in the record")
    while True:
        new_record=input("Enter finish if you are done\n")
        if new_record.lower()=="finish":
            print("Added Successfully")
            break
        else:
            record.append(new_record)
            print("New record added,please continue\n")
        

def update_record():
    show_record()
    while True:
        print("Enter 'x' to exit update menu")
        index_input = input("Enter the index of the chicken to update: ")
        if index_input.lower() == 'x':
            print("Exiting update menu.")
            break
        elif index_input.isdigit():
            index = int(index_input)
            if 0 <= index < len(record):
                 new_name = input("Enter the new chicken name: ")
                 old_name = record[index]
                 record[index] = new_name
                 print(f"{old_name} updated to {new_name}.")
            else:
                print("Invalid index.")
        else:
            print("Please enter a valid number or 'x' to exit.")

def delete_record():
    show_record()
    while True:
        print("\nEnter 'x' to exit delete menu.")
        index_input = input("Enter the index of the chicken to delete: ")

        if index_input.lower() == 'x':
            print("Exiting delete menu.")
            break
        elif index_input.isdigit():
            index = int(index_input)
            if 0 <= index < len(record):
                deleted_name = record.pop(index)
                print(f"{deleted_name} deleted successfully.")
            else:
                print("Invalid index. Please try again.")
        else:
            print("Please enter a valid number or 'x' to exit.")

main_menu()
