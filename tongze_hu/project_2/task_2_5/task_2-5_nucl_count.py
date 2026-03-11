sequence = str(input('Введите последовательность нуклеотидов: '))
sequence = sequence.upper()
sequence_len = len(sequence)

count_A = sequence.count("A")
count_T = sequence.count("T")
count_G = sequence.count("G")
count_C = sequence.count("C")

procent_A = round(count_A / sequence_len * 100, 2)
procent_T = round(count_T / sequence_len * 100, 2)
procent_G = round(count_G / sequence_len * 100, 2)
procent_C = round(count_C / sequence_len * 100, 2)



print(f'''
Последовательность ДНК: {sequence}
Длина последовательности ДНК: {sequence_len}
    
Нуклеотид:\tКоличество:\tПроцентное содержание:
A\t\t{count_A}\t\t{procent_A}
T\t\t{count_T}\t\t{procent_T}
G\t\t{count_G}\t\t{procent_G}
C\t\t{count_C}\t\t{procent_C}
''')