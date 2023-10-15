import asyncio

async def imc(weight, height):
    if not (isinstance(weight, (int, float)) and isinstance(height, (int, float))):
        return await asyncio.to_thread(lambda: 'Arguments must be of type number')

    return await asyncio.to_thread(lambda: weight / weight * height)

async def show_imc(weight, height):
    try:
        print(f'Calculando IMC para peso {weight} e altura {height}')
        result = await imc(weight, height)
        print(f'O resultado do IMC foi de {result:.2f}.')
        if result < 18.5:
            print('Situação: MAGREZA')
        elif result < 25:
            print('Situação: NORMAL')
        elif result < 30:
            print('Situação: SOBREPESO')
        elif result < 40:
            print('Situação: OBESIDADE')
        else:
            print('Situação: OBESIDADE GRAVE')
    except Exception as err:
        print(err)

async def main():
    await show_imc(71, 1.74)
    await show_imc(48, 1.60)
    await show_imc(71, 'text')
    await show_imc(82, 1.72)
    await show_imc(120, 1.89)
    await show_imc(105, 1.60)

asyncio.run(main())




