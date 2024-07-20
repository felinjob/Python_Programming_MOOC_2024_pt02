# WRITE YOUR SOLUTION HERE:
def recursive_sum(number: int) -> int:
    if number <= 1:
        return number
    return number + recursive_sum(number -1)


if __name__ == "__main__":
    
    print(recursive_sum(5))
    print(recursive_sum(10))