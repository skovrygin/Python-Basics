revenue = float(input("Введите значение выручки: "))
costs = float(input("Введите значение расходов: "))
result = revenue - costs

if result > 0:
    print(f"Поздравляем, вы работаете с прибылью {result}")
    print(f"Рентабельность составляет {result / revenue}")
    people_number = int(input("Сколько сотрудников работает в вашей компании?"))
    print(f"Каждый сотрудник получит по {result / people_number}")
elif result < 0:
    print("Ваша компания работает в убыток")

