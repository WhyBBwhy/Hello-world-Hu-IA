# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('wild_boars.csv')
#print(type(df))

with open ("average_characteristics", 'w') as file:
    
    average_age = df['age_years'].mean()
    file.write(f"\nBoars average age is {average_age:.2f} years")
    
    average_weight = df['weight_kg'].mean()
    file.write(f"\nBoars average weight is {average_weight:.2f} kilos")
    
    average_length = df['length_cm'].mean()
    file.write(f"\nBoars average length is {average_length:.2f} cm")
    
    average_shoulder_height = df['shoulder_height_cm'].mean()
    file.write(f"\nBoars average shoulder height is {average_shoulder_height:.2f} cm")
    
    average_tusk_length = df['tusk_length_cm'].mean()
    file.write(f"\nBoars average tusk length is {average_tusk_length:.2f} cm")
    
    average_litter_size = df['litter_size'].mean()
    file.write(f"\nBoars average litter size is {average_litter_size}")
    
    average_health_score = df['health_score'].mean()
    file.write(f"\nBoars average health score  is {average_health_score:.2f}")
    
    average_territory = df['territory_ha'].mean()
    file.write(f"\nBoars average territory is {average_territory:.2f} ha")