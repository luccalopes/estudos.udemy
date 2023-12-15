numero_str = input('vou dobrar o número que vc digitar ')

try:
    print('STR ', numero_str)
    numero_float = float(numero_str)
    print('FLOAT: ', numero_str)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('Isso não é um número')

# numero_int = int(numero_str)

#if numero_str.isdigit(): 
#    numero_float = float(numero_str)
#    print(f'o dobro de {numero_str} é {numero_float * 2}')
#else:
#    print(f'isso não é um número')


# o try/ except funcionam de forma semelhante ao if/else
# quando declaramos um bloco de código dentro do try, o python vai tentar executar este bloco se não houver nada que cause um erro no código, se houver algo errado, ele já cai direto no except