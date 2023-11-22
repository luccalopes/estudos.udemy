# interpolação de strings
# s - string
# d e i - int
# f - float
# x e X = hexadecimal (ABCDEFf0123456789)

nome = 'Lucca'
preco = 123.45678
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (1500, 1500))

# para utilizar a interpolação, basta digitar um sinal de '%' seguido da letra do tipo (float, int, string, hexad. etc)
# a interpolação funciona com as formatações de casas decimais antes aprendidas
# antes dos parâmetros da interpolação dentro dos parenteses no final da linha, deve-se colocar um sinal de '%' também 
# este sinal deve ser colocado fora da string com interpolação
# a letra x converte um float ou int para hexadecimal, para formatá-lo para a quantidade de casas decimais (4 e 8),
# basta inserir um 0 seguido do número desejado - também inserir os números que devem ser convertidos dentro dos 
# parenteses como parametros
