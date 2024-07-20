class Present:
    def __init__(self, name: str, weight: int):  # Corrected type hint for name
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


class Box:
    def __init__(self, presents: list[Present] = None) -> None:  
        self.presents = presents or []  

    def add_present(self, present: Present) -> None:
        self.presents.append(present)

    def total_weight(self) -> int:
        total_weight = 0  
        for present in self.presents:
            total_weight += present.weight  
        return total_weight


if __name__ == "__main__":
    book = Present("ABC Book", 2)
    box = Box()  
    box.add_present(book)
    print(box.total_weight())  

    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight()) 