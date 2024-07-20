# WRITE YOUR SOLUTION HERE:

def add_numbers_to_list(numbers: list) -> list:    
    if len(numbers) % 5 == 0:
        return numbers
    numbers.append(numbers[-1] + 1)
    add_numbers_to_list(numbers)
    

if __name__ == "__main__":
    print(add_numbers_to_list([1,2,3,4]))
