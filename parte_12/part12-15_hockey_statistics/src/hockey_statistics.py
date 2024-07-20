# Write your solution here
import json

class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name
    
    def load_file(self):       
        with open(self.file_name) as file:
            data = file.read()
        players = json.loads(data)        
        return players
        
class HockeyStore:
    def __init__(self, file_name):
        self.file_handler = FileHandler(file_name)
        self.players = self.new_players()
    
    def new_players(self):        
        return [player for player in self.file_handler.load_file()]
                                
class HockeyStats:
    def __init__(self, file_name):
        self.stats = HockeyStore(file_name)
    
    def print_statement(self, variable):
        lista = []
        for p in variable:
            lista.append(f"{p["name"]:21}{p["team"]}{p["goals"]:>4}{"+":>2}{p["assists"]:>3}{"=":>2}{p["goals"] + p["assists"]:>4}")
        return lista
    
    def data_size(self):
        return len(self.stats.players)
    
    def order_by_points(self, items: list) -> list:
        items.sort(key=lambda p: (p["goals"] + p["assists"], p["goals"]), reverse=True)
        return items
    
    def order_by_goals(self, items: list) -> list:
        items.sort(key=lambda p: (p["goals"], -p["games"]), reverse=True)
        return items
    
    def search_player(self, name):
        players = filter(lambda n: n["name"] == name, self.stats.players)
        for item in self.print_statement(players):
            print(item)
        
    def all_teams(self):        
        teams = sorted(list(set(t["team"] for t in self.stats.players)))
        for team in teams:
            print(team)
            
    def all_countries(self):
        countries = sorted(list(set(c["nationality"] for c in self.stats.players)))
        for country in countries:
            print(country)
    
    def players_in_team(self, team: str):
        players = list(filter(lambda p: p["team"] == team, self.stats.players))   
        players = self.order_by_points(players)  
        for item in self.print_statement(players):
            print(item)
        
    def players_in_country(self, country: str):
        players = list(filter(lambda c: c["nationality"] == country, self.stats.players))
        players = self.order_by_points(players)
        for item in self.print_statement(players):
            print(item)
              
    def most_points(self, how_many: int):
        players = self.order_by_points(self.stats.players)
        players = self.print_statement(players)
        for p in range(how_many):
            print(players[p])
            
    def most_goals(self, how_many: int):
        players = self.order_by_goals(self.stats.players)
        players = self.print_statement(players)
        for p in range(how_many):
            print(players[p])
        
class HockeyApp:
    def __init__(self):
        self.stats = HockeyStats(self.add_file())

    def add_file(self):
        file_name = input("file name: ")
        return file_name
        
    def help(self):
        print("commands:")
        print("0 quit")
        print("1 search for player")
        print("2 teams")
        print("3 countries")
        print("4 players in team")
        print("5 players from country")
        print("6 most points")
        print("7 most goals")

    def execute(self):
        print(f"read the data of {self.stats.data_size()} players")
        print()
        self.help()
        while True:
            print()
            command = int(input("command: "))
            if command == 0:
                break
            elif command == 1:
                name = input("name: ")
                self.stats.search_player(name)
            elif command == 2:
                self.stats.all_teams()
            elif command == 3:
                self.stats.all_countries()
            elif command == 4:
                team = input("team: ")
                print()
                self.stats.players_in_team(team)
            elif command == 5:
                country = input("country: ")
                print()
                self.stats.players_in_country(country)
            elif command == 6:
                how_many = int(input("how many: "))
                print()
                self.stats.most_points(how_many)
            elif command == 7:
                how_many = int(input("how many: "))
                print()
                self.stats.most_goals(how_many)
            else:
                continue
            



teste = HockeyApp()
teste.execute()



