class Item:
    luck = 2
    all = []

    def __init__(self,time: int, name="Placer",):
        assert isinstance(time,int) == True, "Not A Number"
        
        self.name = name
        self.time = time
        Item.all.append(self)

    def calculate_total_price(self, x, y):
        return x * y
    def new_time(self):
        self.time = self.time * 5
    def new_luck(self):
        return self.luck * 5

    def __repr__(self):
        return f"Item({self.name},{self.time})"


item1 = Item(5, "FIVE")
item2 = Item(6, "SIX")
item3 = Item(7, "SEVEN")
item4 = Item(8, "EIGHT")
item5 = Item(9, "NINE")
print(Item.all)