# -*- coding: utf-8 -*-
import pandas as pd
df = pd.read_csv('wild_boars.csv')

mean = df.groupby('gender')['tusk_length_cm'].mean()
std = df.groupby('gender')['tusk_length_cm'].std()

cv_male = (std['Male'] / mean['Male']) * 100
cv_female = (std['Female'] / mean['Female']) * 100

with open('coefficient_of_variation_by_genders', 'w') as file:
    file.write(f"Coefficient of variation of tusk lenght among male boars is {cv_male:.2f} %")
    file.write(f"\nCoefficient of variation of tusk lenght among female boars is {cv_female:.2f} %")