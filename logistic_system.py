"""
Logistics system module
"""
LAST_ORDER_ID = 0
ORDERS = []
class Vehicle():
    """
    Represents the vehicle number and its status.
    """
    def __init__(self,vehicle_number,is_available=True):
        self.vehicle_number = vehicle_number
        self.is_available = is_available


class Item():
    """
    Represents the item name and its price.
    """
    def __init__(self,name,price):
        self.name = name
        self.price = price


    def __str__(self):
        """
        Returns information about product in string form.
        """
        return f'Product name: {self.name}, Cost: {self.price}.'


class Location():
    """
    Represents  location and postoffice.
    """
    def __init__(self,city,postoffice):
        self.city = city
        self.postoffice = postoffice


class Order():
    """
    Represents information about the order.
    """
    def __init__(self,user_name,city,postoffice,items):
        global LAST_ORDER_ID
        LAST_ORDER_ID+=1
        self.order_id = LAST_ORDER_ID
        self.user_name = user_name
        self.location = Location(city,postoffice)
        self.items = items
        self.vehicle = None


    def __str__(self):
        """
        Returns information about order number in string form.
        """
        return f'Your order number is {self.order_id}.'


    def calculate_amount(self):
        """
        Returns total price of user`s order.
        """
        total_price = 0
        for i in self.items:
            total_price+=i.price
        return total_price


    def assign_vehicle(self,vehicle):
        """
        Assigns vehicle to deliver user`s order.
        """
        self.vehicle = vehicle


class LogisticSystem():
    """
    Represents the logistic system.
    """
    def  __init__(self,vehicles):
        self.orders = ORDERS
        self.vehicles = vehicles


    def place_order(self,order):
        """
        Assigns vehicle to deliver in order if there are available vehicles
        or returns massage about inaccessibility otherwise.
        """
        for i in self.vehicles:
            if i.is_available:
                ORDERS.append(order)
                i.is_available = False
                order.assign_vehicle(i)
                return
        print("There is no available vehicle to deliver an order.")

    def show_orders(self):
        if self.orders == []:
            print('There are no orders.')
            return
        for i in self.orders:
            items = ''
            for index,item in enumerate(i.items):
                if index != len(i.items)-1:
                    items+=item.name+', '
                else:
                    items+=item.name
            print(f"Order number #{i.order_id}, city {i.location.city}, \
postoffice number #{i.location.postoffice}, items: {items}.")
    def track_order(self,order_id):
        """
        Returns status of order if it exsists or massage of
        its absence otherwise.
        """
        order_index = None
        for i in self.orders:
            if i.order_id == order_id:
                order_index = self.orders.index(i)
        if order_index is None:
            return 'No such order.'
        total_price = self.orders[order_index].calculate_amount()
        return f"Your order #{order_id} is sent to {self.orders[order_index].location.city}. \
Total price: {total_price} UAH."

