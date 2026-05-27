# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('wild_boars.csv')

# Считаем моду для всех числовых колонок
mode = df.mode().iloc[0]

# Отдельно считаем моду выводка только для самок
modes_litter_females = df[df['gender'] == 'Female']['litter_size'].mode()
mode_litter = modes_litter_females.iloc[0] 

with open("mode_characteristics_cycle.txt", 'w') as file:
    file.write("Приводится только одна мода!\n")
    for column, mode_value in mode.items():
        param_name = column.replace('_', ' ')
                
        if column == 'litter_size':
            if pd.notna(mode_litter):
                file.write(f"Boars mode {param_name} (females only) is {mode_litter}\n")
            else:
                file.write(f"Boars mode {param_name} is not available\n")
                
        elif column == 'boar_id':
            continue
        
        else:
            if pd.notna(mode_value):
                file.write(f"Boars mode {param_name} is {mode_value}\n")
            else:
                file.write(f"Boars mode {param_name} is not available\n")