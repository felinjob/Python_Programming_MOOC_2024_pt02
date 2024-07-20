# Write your solution here:
from random import choice

def word_generator(characters: str, length: int, amount: int) -> str:
    for i in range(amount):
        teste = ""
        for p in range(length):
            teste += choice(characters)
        
        yield teste


if __name__ == "__main__":
        
    wordgen = word_generator("abcdefg", 3, 2)
    for word in wordgen:
        print(word)