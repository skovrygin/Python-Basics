while True:
    days = 1
    start_distance = float(input("Введите начальную дистанцию: "))
    last_distance = float(input("Введите конечную дистанцию: "))
    if start_distance < 0 or last_distance < 0:
        print("Введите положительное значение дистанции")
    else:
        while start_distance < last_distance:
            start_distance += start_distance * 0.1
            days += 1

        print(f"Вы добьетесь вашего результата за {days} дней")
        break
