# -*- coding: utf-8 -*-
mport pandas as pd
df = pd.read_csv('wild_boars.csv')
#print(type(df))

with open ("median_characteristics", 'w') as file:
    
    median_age = df['age_years'].median()
    file.write(f"\nBoars median age is {median_age:.2f} years")
    
    median_weight = df['weight_kg'].median()
    file.write(f"\nBoars median weight is {median_weight:.2f} kilos")
    
    median_length = df['length_cm'].median()
    file.write(f"\nBoars median length is {median_length:.2f} cm")
    
    median_shoulder_height = df['shoulder_height_cm'].median()
    file.write(f"\nBoars median shoulder height is {median_shoulder_height:.2f} cm")
    
    median_tusk_length = df['tusk_length_cm'].median()
    file.write(f"\nBoars median tusk length is {median_tusk_length:.2f} cm")
    
    median_litter_size = df['litter_size'].median()
    file.write(f"\nBoars median litter size is {median_litter_size}")
    
    median_health_score = df['health_score'].median()
    file.write(f"\nBoars median health score  is {median_health_score:.2f}")
    
    median_territory = df['territory_ha'].median()
    file.write(f"\nBoars median territory is {median_territory:.2f} ha")