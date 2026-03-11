reagent_name = input('Enter the reagent name >>> ')
number_of_reagents = int(input('Enter the number of reagent >>> '))
report = f'Реактив {reagent_name} поступил на склад в количестве {number_of_reagents} шт.'

with open('C:/Users/user/Documents/Study/Informatic/projects_2/task_2_2/inventory.txt', 'a+', encoding='utf-8') as file:
    print(report, file=file)

print(report)