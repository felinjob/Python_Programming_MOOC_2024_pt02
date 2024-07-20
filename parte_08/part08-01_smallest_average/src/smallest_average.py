lista = "7 - 6 - 8 - 7 - 6 - 4 - 5 - 7 - 7 - 8 - 5 - 10 - 6 - 7 - 8 - 5 - 10 - 4 - 6 - 7 - 7 - 9 - 5 - 6 - 8 - 6 - 7 - 10 - 4 - 6 - 9 - 5 - 8 - 9 - 10 - 7 - 7 - 5 - 9 - 10"

number = lista.split(" - ")

print(number)

menor = 0

for n in number:
    if number.count(n) > menor:
        menor = int(n)
        
print(menor)