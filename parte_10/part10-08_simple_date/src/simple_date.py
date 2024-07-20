# WRITE YOUR SOLUTION HERE:
class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = self.set_day(day)
        self.month = self.set_month(month)
        self.year = self.set_year(year)
        
    def set_day(self, day: int):
        if 1 <= day <= 30:
            return day
        else:
            raise ValueError("Day must be between 1 and 30")
        
    def set_month(self, month: int):
        if 1<= month <= 12:
            return month
        else: 
            raise ValueError("Month must be between 1 and 12")
        
    def set_year(self, year: int):
        if year > 0:
            return year
        else: 
            raise ValueError("Year must be a positive integer")

    def sum_days(self):
        return (self.year * 12 * 30) + (self.month * 30) + self.day
            
    def set_date(self):
        return int(str(self.year) + str(self.month) + str(f"{self.day:02d}"))
    
    def __eq__(self, other: "SimpleDate"):
        return self.set_date() == other.set_date()
    
    def __ne__(self, other: "SimpleDate"):
        return self.set_date() != other.set_date()
    
    def __lt__(self, other: "SimpleDate"):
        return self.set_date() < other.set_date()
    
    def __gt__(self, other: "SimpleDate"):
        return self.set_date() > other.set_date()
        
    def __add__(self, other: int):
        day = self.day
        month = self.month
        year = self.year
        for number in range(other):  
            if day == 30:       
                if month == 12:
                    day = 1
                    month = 0
                    year += 1
                day = 0
                month += 1
            day += 1        
        return SimpleDate(day, month, year)
    
    def __sub__(self, other: "SimpleDate"):
        return abs(self.sum_days() - other.sum_days())
    
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"
        



if __name__ == "__main__":
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)
    d3 = SimpleDate(28, 12, 1985)

    print(d1)
    print(d2)
    print(d1 == d2)
    print(d1 != d2)
    print(d1 == d3)
    print(d1 < d2)
    print(d1 > d2)

    print()
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(28, 12, 1985)

    d3 = d1 + 3
    d4 = d2 + 400

    print(d1)
    print(d2)
    print(d3)
    print(d4)


    print()

    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)

    print(d2-d1)
    print(d1-d2)
    print(d1-d3)
