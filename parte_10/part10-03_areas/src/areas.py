# Write your solution here!
class Rectangle:
    def __init__(self, width: int, height: int):
        self.size = width
        self.height = height

    def __str__(self):
        return f"rectangle {self.size}x{self.height}"

    def area(self):
        return self.size * self.height

class Square(Rectangle):
    def __init__(self, size: int):
        super().__init__(size, size)

    def __str__(self):
        return f"square {self.size}x{self.size}"


if __name__ == "__main__":        
    square = Square(4)  
    print(square)
    print("area:", square.area())