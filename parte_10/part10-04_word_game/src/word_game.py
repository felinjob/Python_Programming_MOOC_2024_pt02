# Write your solution here
import random

class WordGame():
    def __init__(self, rounds: int):
        self.wins1 = 0
        self.wins2 = 0
        self.rounds = rounds

    def round_winner(self, player1_word: str, player2_word: str):
        # determine a random winner
        return random.randint(1, 2)

    def play(self):
        print("Word game:")
        for i in range(1, self.rounds+1):
            print(f"round {i}")
            answer1 = input("player1: ")
            answer2 = input("player2: ")

            if self.round_winner(answer1, answer2) == 1:
                self.wins1 += 1
                print("player 1 won")
            elif self.round_winner(answer1, answer2) == 2:
                self.wins2 += 1
                print("player 2 won")
            else:
                pass # it's a tie

        print("game over, wins:")
        print(f"player 1: {self.wins1}")
        print(f"player 2: {self.wins2}")

class LongestWord(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
        
    def round_winner(self, player1_word: str, player2_word: str):
        return 1 if len(player1_word) > len(player2_word) else 2 if len(player2_word) > len(player1_word) else 0

class MostVowels(WordGame):
    def __init__(self, rounds: int):
        super().__init__(rounds)
    
    def round_winner(self, player1_word: str, player2_word: str):
        vowels = "aeiou"
        player_1 = 0
        player_2 = 0
        for letter in player1_word:
            if letter in vowels:
                player_1 += 1
        for letter in player2_word:
            if letter in vowels:
                player_2 += 1
                
        return 1 if player_1 > player_2 else 2 if player_2 > player_1 else 0
    
class RockPaperScissors(WordGame):
    def __init__(self, round: int):
        super().__init__(round)
        
    def round_winner(self, player1_word: str, player2_word: str):
        word_list = ["rock", "paper", "scissors"]  
        
        if player1_word in word_list and player2_word in word_list:
            if player1_word == player2_word:
                return 0
            elif player1_word == "rock":
                if player2_word == "paper":
                    return 2
                return 1
            elif player1_word == "paper":
                if player2_word == "scissors":
                    return 2
                return 1
            elif player1_word == "scissors":
                if player2_word == "rock":
                    return 2
                return 1
        elif player1_word in word_list and player2_word not in word_list:
            return 1
        elif player2_word in word_list and player1_word not in word_list:
            return 2
        elif player1_word not in word_list and player2_word not in word_list:
            return 0

if __name__ == "__main__":
    p = WordGame(1)
    m = LongestWord(1)
    g = MostVowels(1)
    gg = RockPaperScissors(1)
