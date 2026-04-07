class Stocks:
    def read_details(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def update_price(self,new_price):
        self.price += new_price
    def update_quantity(self,new_quantity):
        self.quantity += new_quantity
    def display(self):
        print("Name:",self.name)
        print("Price:",self.price)
        print("Quantity:",self.quantity)
        print("Total stock price is:",self.quantity*self.price)
s=Stocks()
s.read_details("Laptop",50000,10)
s.update_price(50000)
s.update_quantity(2)
s.display()


