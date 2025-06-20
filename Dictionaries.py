#Print the dictionary key pair value using for loop
person_1={'first_name':'Kiruthika',
          'last_name':'Subramaniam',
          'age': 33,
          'city':'Chennai',
          }
for key,value in person_1.items():
    print(f"{key}:{value}")

numbers={'Kirthi':7,'Karthi':5,'Berni':3,'Mary':8,'priya':6}

for key,value in numbers.items():
    print(f"{key} fav numbers is {value}")

#Print the key and value separately using for loop
Rivers={'Thames':'London',
        'Ganges':'India',
        'Amazon':['Brazil','peru','columbia']
}

for key,value in Rivers.items():
    print(f"{key} runs through {value}")

print("Rivers are \n")
for key in Rivers.keys():
    print(f"\t{key}")

print("Countries are \n")
for value in Rivers.values():
    print(f"\t{value}")

#Store list as value for dictionary and getting the output
favorite_places={'kirthi':['bangalore','kerala','lands end'],
                 'karthi':['chennai','scotland','pune'],
                 'priya':['cardiff','pondicherry','goa']
}

for key,value in favorite_places.items():
    print(f"{key} fav places are {value[0]}, {value[1]} and {value[2]}")

cities={
    'Chennai':{
        'country':'India',
        'population':'6.6 million',
        'fact':'known as singara chennai'
    },
    'Bangalore':{
        'country':'India',
        'population':'8.4 million',
        'fact':'known as garden city'
    },
    'Birmingham':{
        'country':'England',
        'population':'1.16 million',
        'fact':'known as workshop of the world'
    }
}

for city,details in cities.items():
    print(f"The city is {city}\n")
    for key,value in details.items():
        print(f"\tThe {key} is {value}")

glossary={
    'print':' to print some statement',
    'for':'to iterate over a sequence',
    'list':'to store multiple values in variable',
    'if':'to control the flow of execution based on certain conditions',
    'input':'to input the value from user',
}
for key,value in glossary.items():
    print(f"the command {key} is {value.title()}")
