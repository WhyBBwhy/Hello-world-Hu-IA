# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('wild_boars.csv')

# Считаем медиану для всех числовых колонок
median = df.median(numeric_only=True)

# Отдельно считаем медиану размера выводка только для самок
med_litter_females = df[df['gender'] == 'Female']['litter_size'].median()

with open("median_characteristics_cycle.txt", 'w') as file:
    for column, med_value in median.items():
        param_name = column.replace('_', ' ')
                
        if column == 'litter_size':
            if pd.notna(med_litter_females):
                file.write(f"Boars median {param_name} (females only) is {med_litter_females:.2f}\n")
            else:
                file.write(f"Boars median {param_name} is not available\n")
                
        elif column == 'boar_id':
            continue
        
        else:
            if pd.notna(med_value):
                file.write(f"Boars median {param_name} is {med_value:.2f}\n")
            else:
                file.write(f"Boars median {param_name} is not available\n")