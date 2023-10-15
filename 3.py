import csv

file = open("data.csv")
pr = list(csv.reader(file))
print("Нужно купить:")
for i in pr:
    print(f"{i[0]} - {i[1]} шт. за {i[2]} руб.")
print(f"Итоговая сумма: {sum([int(i[1])*int(i[2]) for i in pr])} руб.")
file.close()