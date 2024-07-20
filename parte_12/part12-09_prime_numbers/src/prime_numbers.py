# Write your solution here:
def prime_numbers():
    n = 2
    if n == 2:
        yield n
        n += 1
    while True:
        for number in range(2, n-1):
            if n % number == 0:
                break
        else: 
            yield n
        n += 1 


if __name__ == "__main__":
    
    numbers = prime_numbers()            
                

    for i in range(8):
        print(next(numbers))

    
            