a = 'A'
b = 'B'
c = 1.1
d = 'amo a minha namorada'
string = 'a={0} b={1} c={2:.3f} d={nome4}'
formato = string.format(
    a, b, c, nome4=d
    )


print(formato)

# para capturar os valores dos argumentos, basta inserir um par de chaves correspondente à quantidade de argumentos  
# dentro da função/método
# é possível formatar os números e suas casas decimais, seguindo o modelo da variável c formatada dentro da 
# variável string
# o método format() recebe objetos como argumentos, sendo 2 a mínima quantidade de argumentos
# este método cria uma string que contém campos que serão substituídos pelos argumentos
# neste caso, os argumentos receberam os valores contidos nas variáveis a, b, c e d.
# o número de chaves obrigatoriamente deve ser o mesmo de argumentos, caso contrário a aplicação ira gerar erros
# para não depender da ordem dos valores dos argumentos, basta colocar o índice do elemento dentro das chaves
# porém os índices podem não ser confiáveis
# quando um parametro nomeado for criado, tudo que vier depois deste parametro precisa também ser nomeado
# parametros nomeados devem ser nomeados tanto na string original quanto na string gerada pelo format
# argumentos são chamados aqueles que vêm após o parâmetro nomeado
