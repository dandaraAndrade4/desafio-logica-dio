##feito com python usando input

nome = input("Digite o nome do herói: ")
xp = int(input("Digite o XP do herói: "))

if xp < 1000:
    nivel = "Ferro"
elif xp <= 2000:
    nivel = "Bronze"
elif xp <= 5000:
    nivel = "Prata"
elif xp <= 7000:
    nivel = "Ouro"
elif xp <= 8000:
    nivel = "Platina"
elif xp <= 9000:
    nivel = "Ascendente"
elif xp <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

print(f"O Herói {nome} está no nível de {nivel}")