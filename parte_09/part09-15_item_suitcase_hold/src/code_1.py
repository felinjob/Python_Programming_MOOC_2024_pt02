# Write your solution here:
class Item:
    def __init__(self, name: int, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name
    
    def weight(self):
        return self.__weight
    
    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"
    


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []
        
    def add_item(self, item: Item):
        weight = 0
        for things in self.__items:
            weight += things.weight()
        if (weight + item.weight()) <= self.__max_weight: 
            self.__items.append(item)
    
    def weight(self):
        weight = 0
        for item in self.__items:
            weight += item.weight()
        return weight

    def print_items(self):
        for item in self.__items:
            print(f"{item.name()} ({item.weight()} kg)")
    
    def heaviest_item(self):
        heaviest = None
        for item in self.__items:
            if heaviest == None or item.weight() > heaviest.weight():
                heaviest = item
        return heaviest
    
    def __str__(self):
        if (len(self.__items)) == 0:
            return "0 items (0 kg)"
        elif (len(self.__items)) == 1:
            return f"{len(self.__items)} item ({self.weight()} kg)"
        else:
            return f"{len(self.__items)} items ({self.weight()} kg)"
    

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__suitcases = []
        self.__total_weight = 0
        
    def add_suitcase(self, case: Suitcase):
        if case.weight() + self.__total_weight <= self.__max_weight:
            self.__total_weight += case.weight()
            self.__suitcases.append(case)
    
    def print_items(self):
        for suitcase in self.__suitcases:
            suitcase.print_items()


    def __str__(self):
        if (len(self.__suitcases)) == 1:
            return f"{len(self.__suitcases)} suitcase, space for {self.__max_weight - self.__total_weight} kg"
        
        return f"{len(self.__suitcases)} suitcases, space for {self.__max_weight - self.__total_weight} kg"
        


if __name__ == "__main__":      
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    adas_suitcase = Suitcase(10)
    adas_suitcase.add_item(book)
    adas_suitcase.add_item(phone)

    peters_suitcase = Suitcase(10)
    peters_suitcase.add_item(brick)
    
    cargo_hold = CargoHold(1000)
    cargo_hold.add_suitcase(adas_suitcase)
    cargo_hold.add_suitcase(peters_suitcase)

    print("The suitcases in the cargo hold contain the following items:")
    cargo_hold.print_items()

