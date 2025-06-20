class Restaurant():
    def __init__(self,Restaurant_name,Cuisine_type):
        self.name=Restaurant_name
        self.type=Cuisine_type
        self.number_served=0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.name}")
        print(f"The cuisine type is {self.type}")
        

    def open_restaurant(self):
        print(f"Restaurant {self.name} is open")
    
    def set_number_served(self,number_served):
        self.number_served=number_served
        print(f"the number of customer served {self.number_served}")
    
    def increment_number_served(self,number_served):
        self.number_served+=number_served
        print(f"the number of customer served {self.number_served}")


restaurant1 = Restaurant('Asha','Indian')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.set_number_served(5)
restaurant1.increment_number_served(10)

