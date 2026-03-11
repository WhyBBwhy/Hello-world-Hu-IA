total_volume = float(input('Введите объем раствора (мл): '))
mass_salt = f'{total_volume*0.009:.2f}'
water_volume = total_volume

with open('recipe.txt', 'w', encoding='utf-8') as f:
    f.write(f'''
            ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:
            -----------------------
            Общий объем:\t{total_volume} мл
            Масса соли:\t{mass_salt} г
            Объем воды:\t{water_volume} мл
            ''')