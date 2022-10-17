# Create a class named Pizza with data fields for description (such as sausage
# and onion) and price. Include a constructor that requires arguments for both
# fields and a method to display the data. Create a subclass named DeliveryPizza
# that inherits from Pizza but adds a delivery fee and a delivery address. The
# description, price, and delivery address are required as arguments to the
# constructor. The delivery fee is $3 if the pizza ordered costs more than $15;
# otherwise it is $5. Write an application that instantiates at least two objects of
# each type, and display the values. Save the files as Pizza.java, DeliveryPizza.java,
# and DemoPizzas.java.

class Pizza:
    def __init__(self, description, price):
        self._description = description
        self._price = price

    def get_price(self):
        return self._price

    def print(self):
        print(f"Pizza description: {self._description} , with price  {self._price}")
    

