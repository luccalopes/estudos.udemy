name = 'Lucca'
height = 1.72
weight = 92
imc = weight / (height * height)

print(f'{name} tem {height:.2f} de altura e seu imc é {imc:.2f}')
print(int(imc))


# para usar template literals em Python, usa-se um f antes das aspas de qualquer string, colocando as variáveis dentro # de um par de chaves {}
# para formatar números e escolher a quantia de casas decimais, usa-se os dois pontos seguidos de um ponto (:.),     
# seguido do número desejado e terminando com um f (:.2f)
