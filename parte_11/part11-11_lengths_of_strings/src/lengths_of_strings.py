# WRITE YOUR SOLUTION HERE:
def lengths(strings: list) -> list:
    return {word: len(word) for word in strings}


if __name__ == "__main__":
        
    word_lengths = lengths(word_list)
    print(word_lengths)