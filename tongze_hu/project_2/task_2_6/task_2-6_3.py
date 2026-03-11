phenotype = input("Введите фенотип группы крови (I, II, III, IV): ").strip().upper()
if phenotype == "I":
    print("Можно перелить только группу крови 0 (I)")
elif phenotype == "II":
    print("Можно перелить группы крови: 0 (I) и A (II)")
elif phenotype == "III":
    print("Можно перелить группы крови: 0 (I) и B (III)")
elif phenotype == "IV":
    print("Можно перелить все группы крови")
else:
    print("Такой группы крови не существует")