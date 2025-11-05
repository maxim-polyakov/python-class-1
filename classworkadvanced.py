# Ввод данных от пользователя
purchase_amount = float(input("Введите сумму покупки (в долларах): "))
age = int(input("Введите ваш возраст: "))

# Исходная сумма
original_amount = purchase_amount
discount_applied = False

# Проверка скидки за сумму покупки
if purchase_amount > 100:
    discount = purchase_amount * 0.10
    purchase_amount -= discount
    print(f"Скидка за сумму покупки: ${discount:.2f}")
    discount_applied = True

# Проверка дополнительной скидки за возраст
if age > 65:
    discount = purchase_amount * 0.05
    purchase_amount -= discount
    print(f"Дополнительная скидка за возраст: ${discount:.2f}")
    discount_applied = True

# Вывод результатов
print("\n" + "="*40)
print(f"Исходная сумма: ${original_amount:.2f}")
print(f"Итоговая сумма: ${purchase_amount:.2f}")

if discount_applied:
    total_savings = original_amount - purchase_amount
    print(f"Общая экономия: ${total_savings:.2f}")
else:
    print("Скидки не применялись")