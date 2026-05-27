# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('wild_boars.csv')

# Считаем средние для всех числовых колонок
means = df.mean(numeric_only=True)

# Отдельно считаем средний размер выводка только для самок
avg_litter_females = df[df['gender'] == 'Female']['litter_size'].mean()

with open("average_characteristics_cycle.txt", 'w') as file:
    for column, avg_value in means.items():
        param_name = column.replace('_', ' ')
                
        if column == 'litter_size':
            if pd.notna(avg_litter_females):
                file.write(f"Boars average {param_name} (females only) is {avg_litter_females:.2f}\n")
            else:
                file.write(f"Boars average {param_name} is not available\n")
                
        elif column == 'boar_id':
            continue
        
        else:
            if pd.notna(avg_value):
                file.write(f"Boars average {param_name} is {avg_value:.2f}\n")
            else:
                file.write(f"Boars average {param_name} is not available\n")