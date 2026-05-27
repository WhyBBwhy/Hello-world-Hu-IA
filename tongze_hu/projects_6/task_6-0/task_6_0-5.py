# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('wild_boars.csv')

with open ("percentile_characteristics", "w") as file:
    
    file.write("Age")
    file.write(f"\nPercentile 25 (Q1):\t{df['age_years'].quantile(0.25):.1f} years")
    file.write(f"\nMedian 50 (Q2):\t{df['age_years'].quantile(0.50):.1f} years")
    file.write(f"\nPercentile 75 (Q3):\t{df['age_years'].quantile(0.75):.1f} years")
    file.write(f"\nPercentile 90:\t{df['age_years'].quantile(0.90):.1f} years")
    file.write(f"\nPercentile 95:\t{df['age_years'].quantile(0.95):.1f} years")
    file.write(f"\nMax:\t{df['age_years'].quantile(1.00):.1f} years")
    
    file.write("\n\nShoulder height")
    file.write(f"\nPercentile 25 (Q1):\t{df['shoulder_height_cm'].quantile(0.25):.1f} cm")
    file.write(f"\nMedian 50 (Q2):\t{df['shoulder_height_cm'].quantile(0.50):.1f} cm")
    file.write(f"\nPercentile 75 (Q3):\t{df['shoulder_height_cm'].quantile(0.75):.1f} cm")
    file.write(f"\nPercentile 90:\t{df['shoulder_height_cm'].quantile(0.90):.1f} cm")
    file.write(f"\nPercentile 95:\t{df['shoulder_height_cm'].quantile(0.95):.1f} cm")
    file.write(f"\nMax:\t{df['shoulder_height_cm'].quantile(1.00):.1f} cm")
    
    file.write("\n\nTusk length")
    file.write(f"\nPercentile 25 (Q1):\t{df['tusk_length_cm'].quantile(0.25):.1f} cm")
    file.write(f"\nMedian 50 (Q2):\t{df['tusk_length_cm'].quantile(0.50):.1f} cm")
    file.write(f"\nPercentile 75 (Q3):\t{df['tusk_length_cm'].quantile(0.75):.1f} cm")
    file.write(f"\nPercentile 90:\t{df['tusk_length_cm'].quantile(0.90):.1f} cm")
    file.write(f"\nPercentile 95:\t{df['tusk_length_cm'].quantile(0.95):.1f} cm")
    file.write(f"\nMax:\t{df['tusk_length_cm'].quantile(1.00):.1f} cm")
    
    file.write("\n\nLitter size")
    file.write(f"\nPercentile 25 (Q1):\t{df['litter_size'].quantile(0.25):.1f}")
    file.write(f"\nMedian 50 (Q2):\t{df['litter_size'].quantile(0.50):.1f}")
    file.write(f"\nPercentile 75 (Q3):\t{df['litter_size'].quantile(0.75):.1f}")
    file.write(f"\nPercentile 90:\t{df['litter_size'].quantile(0.90):.1f}")
    file.write(f"\nPercentile 95:\t{df['litter_size'].quantile(0.95):.1f}")
    file.write(f"\nMax:\t{df['litter_size'].quantile(1.00):.1f}")
    
    file.write("\n\nHealth score")
    file.write(f"\nPercentile 25 (Q1):\t{df['health_score'].quantile(0.25):.1f}")
    file.write(f"\nMedian 50 (Q2):\t{df['health_score'].quantile(0.50):.1f}")
    file.write(f"\nPercentile 75 (Q3):\t{df['health_score'].quantile(0.75):.1f}")
    file.write(f"\nPercentile 90:\t{df['health_score'].quantile(0.90):.1f}")
    file.write(f"\nPercentile 95:\t{df['health_score'].quantile(0.95):.1f}")
    file.write(f"\nMax:\t{df['health_score'].quantile(1.00):.1f}")
    
    file.write("\n\nTerritory")
    file.write(f"\nPercentile 25 (Q1):\t{df['territory_ha'].quantile(0.25):.1f} ha")
    file.write(f"\nMedian 50 (Q2):\t{df['territory_ha'].quantile(0.50):.1f} ha")
    file.write(f"\nPercentile 75 (Q3):\t{df['territory_ha'].quantile(0.75):.1f} ha")
    file.write(f"\nPercentile 90:\t{df['territory_ha'].quantile(0.90):.1f} ha")
    file.write(f"\nPercentile 95:\t{df['territory_ha'].quantile(0.95):.1f} ha")
    file.write(f"\nMax:\t{df['territory_ha'].quantile(1.00):.1f} ha")