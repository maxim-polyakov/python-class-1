# Простая версия программы
age = int(input("Введите возраст посетителя: "))

if age < 5:
    price = 0
    category = "ребенок (до 5 лет)"
elif age <= 17:
    price = 10
    category = "ребенок/подросток (5-17 лет)"
else:
    price = 20
    category = "взрослый (18+ лет)"

print(f"\nКатегория: {category}")
print(f"Стоимость билета: ${price}")