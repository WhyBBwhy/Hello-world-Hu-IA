protein_mass = int(input('Введите массу белков в продукте (г): '))
fat_mass = int(input('Введите массу жиров в продукте (г)^ '))
carbohydrates_mass = int(input('Введите масса углеводов в продукте (г)^ '))

print(f'Калорийность: {protein_mass*4 + fat_mass*9 + carbohydrates_mass*4}')
