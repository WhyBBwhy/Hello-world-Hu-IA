number_capsules = int(input('Введите общее количество капсул: '))
capacity_package = int(input('Введите вместимость одной упаковки: '))

full_package = number_capsules//capacity_package
remainig_capsules = number_capsules%capacity_package

print(f'''
    --- Отчет фасовочного цеха ---
    Полных упаковок:\t{full_package}
    Остаток капсул:\t{remainig_capsules}
    ''')
