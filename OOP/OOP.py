import csv

class Item:
    tax_rate = 0.06
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        # Validations on recieved arguments
        assert price >= 0, f"{price} is not greater than, or equal to 0"
        assert quantity >= 0, f"{quantity} is not greater than, or equal to 0"
        assert isinstance(name,str), f"{name} must be a string"
        
        # Asign to self object
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def sold(self, amount_sold):
        self.quantity = self.quantity - amount_sold

    def inventory(self):
        if self.quantity <= 0:
            print(f"{self.name} is currently out of stock")
        else:
            print(f"Current Inventory {self.quantity}")

    def sale(self):
        self.price = self.price * self.tax_rate

    @classmethod
    def get_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name = item.get("name"),
                price = float(item.get("price")),
                quantity = int(item.get("quantity"))
                )

    def __repr__(self):
        return f"Item('{self.name}',{self.price}, {self.quantity})"

Item.get_from_csv()
print(Item.all)