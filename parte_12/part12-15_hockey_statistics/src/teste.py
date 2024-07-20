pessoas = [
    {"nome": "Maria", "idade": 30},
    {"nome": "João", "idade": 25},
    {"nome": "Ana", "idade": 35},
    {"nome": "João", "idade": 20}
]

# Ordenar pessoas por nome e, em seguida, por idade
pessoas.sort(key=lambda x: (x["nome"], x["idade"]))

# Mostrar pessoas ordenadas
for pessoa in pessoas:
    print(pessoa)
    
pessoas = [
    {"nome": "Maria", "idade": 30, "altura": 160, "peso": 60},
    {"nome": "João", "idade": 25, "altura": 170, "peso": 70},
    {"nome": "Ana", "idade": 35, "altura": 165, "peso": 65},
    {"nome": "João", "idade": 20, "altura": 175, "peso": 75}
]

# Ordenar pessoas por nome, idade, altura e peso
pessoas.sort(key=lambda x: (x["nome"], x["idade"], x["altura"], x["peso"]))

# Mostrar pessoas ordenadas
for pessoa in pessoas:
    print(pessoa)
    
    
      
# test = HockeyStats("partial.json")

# print("nome: \n")
# nome = test.search_player("Travis Zajac")
# print()
# print("times: \n")
# team = test.all_teams()
# print()
# print("paises: \n")
# country = test.all_countries()
# print()
# print("jogadores no time \n")
# p_in_t = test.players_in_team("OTT")
# print()
# print("jogadores no país \n")
# p_in_c = test.players_in_country("CAN")
# print()
# print("mais pontos \n")
# most_points = test.most_points(6)

