variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{+1000.378378346:+,.2f}')

# > significa que vai ter 10 espaços vazios à direita da string da variavel
# < significa que vai ter 10 espaços vazios à esquerda da string
# ^ significa que estamos pedindo para encaixar a string da variável no meio de 10 espaços vazios
# para indicar se um número int ou float é positivo ou negativo, utilizar os sinais + ou - após abrir as chaves
# das f'strings, antes do número e após o número, inserir : e depois o sinal