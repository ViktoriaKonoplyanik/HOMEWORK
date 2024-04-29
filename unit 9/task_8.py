
import json
import csv
import os


def create_json_file(data, json_file="employees.json"):
    """Создает JSON-файл с предоставленными данными."""
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=4)


def json_to_csv(json_file="employees.json", csv_file="employees.csv"):
    """Конвертирует данные из JSON-файла в CSV-файл."""
    with open(json_file, 'r') as f:
        data = json.load(f)

    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)


def save_to_csv(data, csv_file="employees.csv"):
    """Сохраняет данные в CSV-файл, обрабатывая переменную длину данных."""
    with open(csv_file, 'w', newline='') as f:
        if data:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


def add_employee_json(json_file="employees.json"):
    """Добавляет нового сотрудника в JSON-файл."""
    with open(json_file, 'r+') as f:
        data = json.load(f)
        new_employee = {}
        new_employee["name"] = input("Введите имя сотрудника: ")
        new_employee["birthday"] = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
        new_employee["height"] = int(input("Введите рост (см): "))
        new_employee["weight"] = float(input("Введите вес (кг): "))
        new_employee["car"] = input("Есть ли автомобиль? (да/нет): ").lower() == "да"
        languages = input("Введите языки программирования (через запятую): ")
        new_employee["languages"] = [lang.strip() for lang in languages.split(",")]
        data.append(new_employee)
        f.seek(0)
        json.dump(data, f, indent=4)


def add_employee_csv(csv_file="employees.csv"):
    """Добавляет нового сотрудника в CSV-файл."""
    with open(csv_file, 'a', newline='') as f:
        fieldnames = ["name", "birthday", "height", "weight", "car", "languages"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        new_employee = {}
        new_employee["name"] = input("Введите имя сотрудника: ")
        new_employee["birthday"] = input("Введите дату рождения (ДД.ММ.ГГГГ): ")
        new_employee["height"] = int(input("Введите рост (см): "))
        new_employee["weight"] = float(input("Введите вес (кг): "))
        new_employee["car"] = input("Есть ли автомобиль? (да/нет): ").lower() == "да"
        languages = input("Введите языки программирования (через запятую): ")
        new_employee["languages"] = languages
        writer.writerow(new_employee)


def get_employee_by_name(data, name):
    """Получает информацию о сотруднике по имени."""
    for employee in data:
        if employee["name"] == name:
            return employee
    return None


def filter_by_language(data, language):
    """Фильтрация сотрудников по языку программирования."""
    return [employee for employee in data if language in employee["languages"]]


def filter_by_birth_year(data, year):
    """Фильтрация сотрудников по году рождения и расчет среднего роста."""
    filtered_employees = [employee for employee in data if int(employee["birthday"].split(".")[2]) < year]
    if filtered_employees:
        heights = [employee["height"] for employee in filtered_employees]
        return sum(heights) / len(heights)
    else:
        return None


def main():
    """Главная функция с интерактивным меню."""

    # Создание JSON-файла с начальными данными
    if not os.path.exists("employees.json"):
        initial_data = [
            {
                "name": "John Smith",
                "birthday": "02.10.1990",
                "height": 175,
                "weight": 76.5,
                "car": True,
                "languages": ["C++", "Python"]
            },
            {
                "name": "Alexey Alexeev",
                "birthday": "05.06.1986",
                "height": 197,
                "weight": 101.2,
                "car": False,
                "languages": ["Pascal", "Delphi"]
            },
            {
                "name": "Maria Ivanova",
                "birthday": "28.08.1998",
                "height": 165,
                "weight": 56.1,
                "car": True,
                "languages": ["C#", "C++", "C"]
            }
        ]

        create_json_file(initial_data)

    while True:
        print("\nВыберите действие:")
        print("1. Конвертировать JSON в CSV")
        print("2. Добавить сотрудника в JSON")
        print("3. Добавить сотрудника в CSV")
        print("4. Поиск сотрудника по имени")
        print("5. Фильтр по языку программирования")
        print("6. Фильтр по году рождения (средний рост)")
        print("7. Выход")

        choice = input("Выберите путь: ")

        if choice == "1":
            json_to_csv()
            print("Данные конвертированы в CSV.")
        elif choice == "2":
            add_employee_json()
            print("Сотрудник добавлен в JSON.")
        elif choice == "3":
            add_employee_csv()
            print("Сотрудник добавлен в CSV.")
        elif choice == "4":
            name = input("Введите имя сотрудника: ")
            with open("employees.json", 'r') as f:
                data = json.load(f)
            employee = get_employee_by_name(data, name)
            if employee:
                print(employee)
            else:
                print("Сотрудник не найден.")
        elif choice == "5":
            language = input("Введите язык программирования: ")
            with open("employees.json", 'r') as f:
                data = json.load(f)
            filtered_employees = filter_by_language(data, language)
            if filtered_employees:
                for employee in filtered_employees:
                    print(employee)
            else:
                print("Сотрудники не найдены.")
        elif choice == "6":
            year = int(input("Введите год рождения: "))
            with open("employees.json", 'r') as f:
                data = json.load(f)
            avg_height = filter_by_birth_year(data, year)
            if avg_height:
                print("Средний рост:", avg_height)
            else:
                print("Сотрудники не найдены.")
        elif choice == "7":
            break
        else:
            print("Неверный выбор.")


if __name__ == "__main__":
    main()

