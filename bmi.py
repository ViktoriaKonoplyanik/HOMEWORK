try:
    # Получаем рост и вес от пользователя
    height_cm = float(input("Введите ваш рост в сантиметрах: "))
    if height_cm <= 0:
        raise ValueError("Рост должен быть положительным числом")

    weight_kg = float(input("Введите ваш вес в килограммах: "))
    if weight_kg <= 0:
        raise ValueError("Вес должен быть положительным числом")

    # Вычисляем ИМТ
    bmi = weight_kg / ((height_cm / 100) ** 2)

    # Интерпретируем результаты
    if bmi < 18.5:
        print("Ваш ИМТ:", bmi)
        print("Пояснение: Недостаточный вес")
    elif bmi >= 18.5 and bmi < 25:
        print("Ваш ИМТ:", bmi)
        print("Пояснение: Нормальный вес")
    elif bmi >= 25 and bmi < 30:
        print("Ваш ИМТ:", bmi)
        print("Пояснение: Избыточный вес")
    elif bmi >= 30 and bmi < 35:
        print("Ваш ИМТ:", bmi)
        print("Пояснение: Ожирение первой степени")
    elif bmi >= 35 and bmi < 40:
        print("Ваш ИМТ:", bmi)
        print("Пояснение: Ожирение второй степени")
    else:
        print("Ваш ИМТ:", bmi)
        print("Пояснение: Ожирение третьей степени")

except ValueError:
    print("Ошибка: введены некорректные данные")
except ZeroDivisionError:
    print("Ошибка: рост не может быть равен нулю")