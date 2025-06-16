#Dinner Invite using list

Invite=["Sherin","Mary","Paula","Deepa"]
for guest in Invite:
    print(f"Hi {guest} ,This saturday night,party at my place")

not_available=Invite.pop(0)
Invite.insert(0,"Dominic")
print(f"Name of the guests who can't make it, {not_available}")
for guest in Invite:
    print(f"Hi {guest} ,This saturday night,party at my place")
print(Invite)
print("Inviting more people")
Invite.append('Balaji')
Invite.insert(3,"Karanjith")
Invite.insert(0,"Bernie")
print(Invite)
for guest in Invite:
    print(f"Hi {guest} ,This saturday night,party at my place")


print("Inviting onle 2 people")

for guest in range(len(Invite)-1,1,-1):
    cancel=Invite.pop(guest)
    print(f"Sorry {cancel} ,Invitation has been cancelled")
    print(Invite)


for guest in Invite:
    print(f"Hi {guest} still invited,This saturday night,party at my place")

print(Invite)



for guest in range(len(Invite)-1,-1,-1):
     del Invite[guest]
     print(Invite)

    
print(len(Invite))

#Q5
places=["Home","Kerala","Lands end","Bangalore","London"]
print(places) #Print your list in its original order

print(sorted(places)) #alphabetical order without modifying the actual list

print(places) #still in original order


print(sorted(places,reverse=True)) #sorted() to print your list in reverse alphabetical order

print(places) #still in original order

places.reverse() # reverse() to change the order of your list
print(places)

places.reverse() #Use reverse() to change the order of your list again
print(places)

places.sort() #Use sort() to change your list so it’s stored in alphabetical orde
print(places)

places.sort(reverse=True) #Use sort() to change your list so it’s stored in reverse alphabetical order
print(places)
