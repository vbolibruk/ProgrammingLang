# Create a class named Pizza with data fields for description (such as sausage
# and onion) and price. Include a constructor that requires arguments for both
# fields and a method to display the data. Create a subclass named DeliveryPizza
# that inherits from Pizza but adds a delivery fee and a delivery address. The
# description, price, and delivery address are required as arguments to the
# constructor. The delivery fee is $3 if the pizza ordered costs more than $15;
# otherwise it is $5. Write an application that instantiates at least two objects of
# each type, and display the values. Save the files as Pizza.java, DeliveryPizza.java,
# and DemoPizzas.java.

from Pizza import Pizza

class DeliveryPizza(Pizza):
    all_pizzas = []

    def __init__(self, description, price , deliveryAddress):
        super().__init__(description, price)
        self.__class__.all_pizzas.append(self)

        self._deliveryFee = 0
        if(self.total_cost() > 15):
            self._deliveryFee += 3
        else: 
            self._deliveryFee = 5
        self._deliveryAddress = deliveryAddress

    def print(self):
        print(f"Pizza description: {self._description} , with price  {self._price},deliveryFee :  {self._deliveryFee} ,deliveryAddress : {self._deliveryAddress} ")
   
    @classmethod
    def total_cost(cls): 
        total = 0
        for c in cls.all_pizzas: 
                    total = total + c.get_price()
        return total
