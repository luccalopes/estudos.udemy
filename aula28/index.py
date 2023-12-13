complete_name = input('Digite seu nome completo: ')
age = input('Digite o número da sua idade: ')

if complete_name and age:
    print(f'Seu nome é {complete_name}')
    print(f'Seu nome invertido é: {(complete_name[::-1])}')

    if ' ' in complete_name:
        print(f'{complete_name} tem espaços')
    else:
        print(f'{complete_name} não contém espaços')
    print(f'Seu nome tem {len(complete_name)} letras.')
    print(f'A primeira letra do seu nome é: {complete_name[0]}')
    print(f'A última letra do seu nome é: {complete_name[-1]}')
else:
    print('nada foi digitado')

