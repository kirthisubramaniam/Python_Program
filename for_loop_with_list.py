#Using for loop index method to print
fav_pizza=["Chicken supreme","Bombay Veg","Margherita pizza"]
for pizza in fav_pizza:
    print(f"My favourite pizza is {pizza}")

print(f"My all time fav pizza is {fav_pizza[0]},{fav_pizza[1]} and {fav_pizza[2]}.\nI like to add extra topping like chilli,olives and jalapenos.\nNo party withut pizza")

#Using for loop to print 
animals=["pola bear","panda","penguin"]
for animal in animals:
    print(animal)

#List the number using for loop
for number in range(1,21,+1):
    print(number)

#Display how to use min,max and sum of int
Number=list(range(1,1000001))

print(min(Number))
print(max(Number))
print(sum(Number))

#Example to show how a list grow from empty list
friends_pizza=fav_pizza[:]
print(friends_pizza)

fav_pizza.append("pepperoni")
friends_pizza.append("Meat feast")

print(fav_pizza)
print(friends_pizza)

print("My Fav pizzas are")
for pizza in fav_pizza:
    print(pizza)
print("My friend's fav pizza")
for pizza in friends_pizza:
    print(pizza)






