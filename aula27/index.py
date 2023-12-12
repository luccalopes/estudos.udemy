variavel = 'Olá mundo'
# print(variavel[0:5])
print(variavel[0:len(variavel):1])

# podemos fatiar as strings com o início, o fim e um passo i:f:p 
# para escolher a fatia da string, utilizaremos os índices de 0 a 9 ou do -9 ao -1
# se eu quiser fatiar a string do começo ao meio, utilizar do índice 0 até o índice que corresponde à metade da string
# se eu quiser deixar explícito que a string deve começar do índice 0, posso simplesmente omitir esse índice de começo, indicando apenas onde a fatia deve terminar
# o mesmo acontece ao contrário, posso omitir o índice final da fatia se ele representar o último índice da string
# se eu quiser indicar um final para esta fatia que não corresponda ao final da string original, deve-se sempre contar um índice a mais 
# (exemplo: 0:5 em 'olá mundo representa o quarto índice na string iterável, ou seja, o espaço em branco então a fatia teria uma saída de 'olá m)
# 012345678
# Olá mundo
#-987654321