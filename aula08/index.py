name = 'Lucca'
surname = 'Lopes'
girlfriend = 'Bianca'
gf_surname = 'Neme'
age = 27
gf_age = 26
birthday = 2023 - age
gf_birthday = 2023 - gf_age
majority = age >= 18 and gf_age >= 18
height_meters = 1.72

print('Nome:', name)
print('Sobrenome:', surname)
print('Namorada:', girlfriend)
print('Sobrenome da namorada:', gf_surname )
print('Idade:', age, gf_age)
print('Maiores de idade?', majority)
print('Altura em metros:', height_meters)
print(birthday, gf_birthday)


