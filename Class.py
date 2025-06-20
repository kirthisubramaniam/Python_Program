#Program that tracks the number of login using class and function
class User():
    def __init__(self,first_name,last_name,place,age,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.place=place
        self.age=age
        self.login_attempts=login_attempts
    
    def describe_user(self):
        print(f"{self.first_name},{self.last_name},{self.place},{self.age}")

    def greet_user(self):
        print(f"welcome {self.first_name} {self.last_name}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"login attempt:{self.login_attempts}")
    
    def reset_login_attempts(self):
        self.login_attempts=0
        print(f"reset value :{self.login_attempts}")


user1=User('Kiruthika','Subramaniam','Birmingham',32,0)
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()

#Program calling class and function multiple times to get output of different attribute.
class Car():
    def __init__(self,make,model,year,mileage=0):
        self.make=make
        self.model=model
        self.year=year
        self.mileage=mileage
        

    def get_mileage(self,mileage):
        self.mileage=mileage
    
    def get_info(self):
        print(f"Details are {self.make},{self.model},{self.year},{self.mileage} miles")

car1=Car('Ford','Fiesta',2022)
car2=Car('Toyota','Cororlla',2021)
car3=Car('Honda','Civic',2020)
car4=Car('BMW','3 Series',2019)

car1.get_mileage(10000)
car3.get_mileage(20000)
car2.get_mileage(15000)
car4.get_mileage(25000)
car1.get_info()
car2.get_info()
car3.get_info()
car4.get_info()


class Book():
    
    def __init__ (self,title,author,genre,no_of_pages=0):
        self.title=title
        self.author=author
        self.genre=genre
        self.page_details=no_of_pages
    
    def get_pages_details(self,page_details):
        self.page_details=page_details
    
    def display_info(self):
        print(f"Details of the book are:\n\tTitle:{self.title}\tAuthor:{self.author}\tGenre:{self.genre}\tPages:{self.page_details}")

book1=Book('The Hobbit','J.R.R.Tolkien','Fantasy')
book2=Book('Moby-Dick','Herman Melville','Adventure')
book3=Book('The Lord of the Rings','J.R.R Tolkien','Fantasy')
book4=Book('Brave New Worls','Aldous Huxley','Science Fiction')

book1.get_pages_details(310)
book2.get_pages_details(635)
book3.get_pages_details(1178)
book4.get_pages_details(311)

book1.display_info()
book2.display_info()
book3.display_info()
book4.display_info()

