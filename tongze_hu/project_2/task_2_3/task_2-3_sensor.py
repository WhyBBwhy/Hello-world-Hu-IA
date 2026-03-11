FIO = input('Введите имя оператора: ')
pressure = input('Введите текущее значение давления (Па)')

with open('sensor_log.txt', 'w', encoding='utf-8') as sensor:
    sensor.write(f'Имя оператора\t{FIO}')
    sensor.write(f'Давление\t{pressure}')