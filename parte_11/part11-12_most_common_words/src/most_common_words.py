# WRITE YOUR SOLUTION HERE:

def most_common_words(filename: str, lower_limit: int) -> dict:
    with open(filename, "r") as file:
        text = file.read()
        forbidden = "!?:,."
        texto = "".join([character for character in text if character not in forbidden])
        lista = [word for word in texto.split()]
        return {word: lista.count(word) for word in lista if lista.count(word) >= lower_limit}

    

if __name__ == "__main__":
    most_common_words()
    
