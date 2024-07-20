# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        return f"{self._euros}.{self._cents:02d} eur"

    def __eq__(self, another: "Money"):
        self_value = self._euros + (self._cents / 100)
        another_value = another._euros + (another._cents / 100)
        return self_value == another_value
    
    def __lt__(self, another: "Money"):
        self_value = self._euros + (self._cents / 100)
        another_value = another._euros + (another._cents / 100)
        return self_value < another_value
    
    def __gt__(self, another: "Money"):
        self_value = self._euros + (self._cents / 100)
        another_value = another._euros + (another._cents / 100)
        return self_value > another_value
    
    def __ne__(self, another: "Money"):
        self_value = self._euros + (self._cents / 100)
        another_value = another._euros + (another._cents / 100)
        return self_value != another_value
    
    def __add__(self, another: "Money"):
        self_value = self._euros + (self._cents / 100)
        another_value = another._euros + (another._cents / 100)
        return f"{self_value + another_value:.2f} eur"
        
    def __sub__(self, another: "Money"):
        self_value = self._euros + (self._cents / 100)
        another_value = another._euros + (another._cents / 100)
        if self_value - another_value < 0:
            raise ValueError("a negative result is not allowed")
        return f"{self_value - another_value:.2f} eur"
    

if __name__ == "__main__":
   
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    e4 = e1 - e2

    print(e3)
    print(e4)

    e5 = e2-e1

