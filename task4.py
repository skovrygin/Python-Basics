initial_number = int(input("Введите целое положительное число"))
greatest_digit = initial_number % 10
num = initial_number

while num > 0:
    digit = num % 10
    if digit > greatest_digit:
        greatest_digit = digit
        if greatest_digit == 9:
            break
    num = num // 10

    print(f"Наибольшая цифра числа {initial_number} это {greatest_digit}")
