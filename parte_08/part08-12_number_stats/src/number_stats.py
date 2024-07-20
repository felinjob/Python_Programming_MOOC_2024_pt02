# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)

    def get_sum(self):
        if len(self.numbers) == 0:
            return 0
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) == 0:
            return 0
        return sum(self.numbers) / len(self.numbers)

def main():
    stats = NumberStats()
    odd = []
    even = []
    while True:
        number = int(input("Please type in integers numbers: "))
        if number == -1:
            break
        stats.add_number(number)

    for number in stats.numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    print(f"Sum of even numbers: {sum(even)}")
    print(f"Sum of odd numbers: {sum(odd)}")


main()