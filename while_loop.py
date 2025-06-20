#Simple while loop to get input from user
prompt="What kind of rental car you would like?\n"

while True:
    car_name=input(prompt)
    print(f"Let me see if i can find you a {car_name}")
    break
print("Thanks for contacting us")

#Different scenario that check some conditions,in continuous loop till it is true
prompt="How many people in their dinner group?\n"

while True:
    no_of_people=int(input(prompt))
    if no_of_people <= 8:
        print("your table is ready")
        break
    elif no_of_people >8:
        print("You will have to wait for a table")
        print("Do you like to wait")
        reply=input("Type yes or No\n")
        if reply.lower()=='yes':
            print("Thanks for your patience")
            break
        else:
            print("Thanks for contacting us")
            break

while True:
    number=int(input("Enter a number \n"))
    if number%10==0:
        print("The number is multiple of 10")
        break
    elif number==0:
        break
    else :
        print("Number is not multiple of 10")
       
print("Thanks")

while True:
    prompt="Enter the age\n"
    age=int(input(prompt))
    if age <3:
        print("Tickets are free")
        break
    elif 3>=age<=12:
        print("Ticke cost is $10")
        break
    elif age >12:
        print("Ticket costis $15")
        break
print("Booking completed")

#Using while loop to check some condition in list datatype

print("Make your own pizza")
available_toppings=['cheese','chicken','onion','olives','tomato','jalapenos','peppers','chillies']
selected_toppings=[]
print(available_toppings)

while True:
    toppings =input("Enter your pizza toppings,enter quit if you are finished\n")
    if toppings.lower() == 'quit':
        break
    elif toppings.lower() in available_toppings:
        selected_toppings.append(toppings)
    else:
        print(f"select from this {available_toppings}")

print(selected_toppings)


sandwich_orders=['egg','pastrami','chicken','pastrami','tuna','tofu','pastrami']
finished_sandwiches=[]
print("Deli has run out of pastrami")

while sandwich_orders:
    current_sandwich=sandwich_orders.pop(0)
    if current_sandwich != 'pastrami':
        print(f"{current_sandwich} is completed")
        finished_sandwiches.append(current_sandwich)
    
        
for sandwich in finished_sandwiches:
    print(f"{sandwich} sandwich")







       
     


