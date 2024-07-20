# WRITE YOUR SOLUTION HERE:
class ListHelper:
    
    @classmethod
    def greatest_frequency(cls, my_list: list):
        greatest = 0
        for number in my_list:
            if my_list.count(number) > my_list.count(greatest):
                greatest = number
                
        return greatest
    
    @classmethod
    def doubles(cls, my_list: list):
        count = 0
        viewed = []
        for number in my_list:
            if my_list.count(number) > 1 and number not in viewed:
                count += 1
                viewed.append(number)
                
        return count
    
    

if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))
