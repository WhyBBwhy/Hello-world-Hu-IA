# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('wild_boars.csv')

# Считаем средние для всех числовых колонок
var = df.var(numeric_only=True)
std = df.std(numeric_only=True)
co_var = (std / var) * 100

# Отдельно считаем всё о выводке для самок
var_litter_females = df[df['gender'] == 'Female']['litter_size'].var()
std_litter_females = df[df['gender'] == 'Female']['litter_size'].std()
co_var_litter_females = (std_litter_females / var_litter_females) * 100

with open("variation_characteristics_cycle.txt", 'w') as file:
    
    file.write("Variation is the following:\n")
    for column, var_value in var.items():
        param_name = column.replace('_', ' ')
                
        if column == 'litter_size':
            if pd.notna(var_litter_females):
                file.write(f"Boars variation of {param_name} (females only) is {var_litter_females:.2f}\n")
            else:
                file.write(f"Boars variation of {param_name} is not available\n")
                
        elif column == 'boar_id':
            continue
        
        else:
            if pd.notna(var_value):
                file.write(f"Boars variation of {param_name} is {var_value:.2f}\n")
            else:
                file.write(f"Boars variation of {param_name} is not available\n")
    
    file.write("\nStandart deviation is the following:\n")
    for column, std_value in std.items():
        param_name = column.replace('_', ' ')
                
        if column == 'litter_size':
            if pd.notna(std_litter_females):
                file.write(f"Boars standart deviiation of {param_name} (females only) is {std_litter_females:.2f}\n")
            else:
                file.write(f"Boars standart deviation of {param_name} is not available\n")
                
        elif column == 'boar_id':
            continue
        
        else:
            if pd.notna(std_value):
                file.write(f"Boars standart deviation of {param_name} is {std_value:.2f}\n")
            else:
                file.write(f"Boars standart deviation of {param_name} is not available\n")
                
    file.write("\nCoefficient of variation is the following:\n")
    for column, co_var_value in co_var.items():
        param_name = column.replace('_', ' ')
                
        if column == 'litter_size':
            if pd.notna(co_var_litter_females):
                file.write(f"Boars coefficient of variation of {param_name} (females only) is {co_var_litter_females:.2f}\n")
            else:
                file.write(f"Boars coefficient of variation {param_name} is not available\n")
                
        elif column == 'boar_id':
            continue
        
        else:
            if pd.notna(co_var_value):
                file.write(f"Boars coefficient of variation of {param_name} is {co_var_value:.2f}\n")
            else:
                file.write(f"Boars coefficient of variation {param_name} is not available\n")