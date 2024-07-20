# WRITE YOUR SOLUTION HERE:

def begin_with_vowel(words: list):
    return [word for word in words if word[0] in "aeiouAEIOU"]

if __name__ == "__main__":
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)