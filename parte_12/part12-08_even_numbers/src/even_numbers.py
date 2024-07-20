# Write your solution here
def even_numbers(beginning: int, maximum: int) -> int:
    number = beginning
    while number <= maximum:
        if number % 2 == 0:
            yield number 
        number += 1
