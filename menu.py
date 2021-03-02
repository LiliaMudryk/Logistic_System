"""
Menu module for notebook
"""
import sys
from logistic_system import LogisticSystem,Vehicle,Item,Order
class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self,items):
        self.items = items
        self.choices = {
            "1": self.show_items_information,
            "2": self.make_order,
            "3": self.show_all_orders,
            "4": self.track_order,
            "5": self.quit
            }


    def display_menu(self):
        """
        Displays menu.
        """
        print("""
Menu
1. Show all items
2. Make order
3. Show all orders
4. Track order
5. Quit
""")


    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))


    def show_items_information(self):
        """
        Displays information about all items.
        """
        for i,elem in enumerate(self.items):
            print(f'{i}: {elem}')

    def make_order(self):
        """
        Asks user for some information to make an order.
        """
        name = input("Enter your name: ")
        city = input("Enter your city: ")
        postoffice = int(input("Enter postofiice number: "))
        self.show_items_information()
        choice = input("Enter numbers of products you want to buy(e.g. 1,2,3): ").split(",")
        items = []
        for i in choice:
            items.append(self.items[int(i)])
        order = Order(name,city,postoffice,items)
        logSystem.place_order(order)
        print(order)


    def show_all_orders(self):
        """
        Displays all orders.
        """
        logSystem.show_orders()


    def track_order(self):
        """
        Displays information about status of user order.
        """
        order_id = int(input("Enter order id: "))
        print(logSystem.track_order(order_id))


    def quit(self):
        """
        Exits programm.
        """
        print("Thank you for using your logistic system today.")
        sys.exit(0)

if __name__ == "__main__":
    vehicles = [Vehicle(1), Vehicle(2)]
    logSystem = LogisticSystem(vehicles)
    my_items = [Item('book',110), Item('chupachups',44), Item('flowers',11), Item('shoes',153),
               Item('helicopter',0.33), Item('coat',61.8), Item('shower',5070), Item('rollers',700)]
    Menu(my_items).run()
