from Pizza import Pizza
from DeliveryPizza import DeliveryPizza



pizzaInHouse_one =  Pizza("SPICY_WITH_MEAT",10)
pizzaInHouse_two =  Pizza("SPICY_VEGAN",9)

pizzaInHouse_one.print()
pizzaInHouse_two.print()


pizzaDelivery_one =  DeliveryPizza("SPICY_WITH_MEAT",10, "GD_85")
pizzaDelivery_one.print()
pizzaDelivery_two =  DeliveryPizza("SPICY_VEGAN",9,"GD_85")
pizzaDelivery_two.print()
print(pizzaDelivery_two.total_cost())
print(pizzaDelivery_one.total_cost())
