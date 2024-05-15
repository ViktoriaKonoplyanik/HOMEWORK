
class Bus:
    def __init__(self, max_passengers, max_speed):
        self.speed = 0
        self.max_passengers = max_passengers
        self.max_speed = max_speed
        self.passengers = []
        self.available_seats = True
        self.seats = {i: None for i in range(1, max_passengers + 1)}  # Словарь мест

    def board_passenger(self, *passengers):
        """Посадка одного или нескольких пассажиров."""
        for passenger in passengers:
            if len(self.passengers) < self.max_passengers:
                self.passengers.append(passenger)
                #  первое свободное место и занимаем его
                for seat_number, occupant in self.seats.items():
                    if occupant is None:
                        self.seats[seat_number] = passenger
                        break
            else:
                print(f"Автобус полон, пассажир {passenger} не может войти.")
        self.available_seats = len(self.passengers) < self.max_passengers

    def disembark_passenger(self, *passengers):
        """Высадка одного или нескольких пассажиров."""
        for passenger in passengers:
            if passenger in self.passengers:
                self.passengers.remove(passenger)
                # Освобождаем место, занятое пассажиром
                for seat_number, occupant in self.seats.items():
                    if occupant == passenger:
                        self.seats[seat_number] = None
                        break
            else:
                print(f"Пассажир {passenger} не найден в автобусе.")
        self.available_seats = len(self.passengers) < self.max_passengers

    def increase_speed(self, value):
        """Увеличение скорости."""
        self.speed = min(self.speed + value, self.max_speed)

    def decrease_speed(self, value):
        """Уменьшение скорости."""
        self.speed = max(self.speed - value, 0)

    def __contains__(self, passenger):
        """Операция in - проверка наличия пассажира в автобусе."""
        return passenger in self.passengers

    def __iadd__(self, passenger):
        """Операция += - посадка пассажира."""
        self.board_passenger(passenger)
        return self

    def __isub__(self, passenger):
        """Операция -= - высадка пассажира."""
        self.disembark_passenger(passenger)
        return self

# Пример использования
bus = Bus(max_passengers=20, max_speed=120)

bus.board_passenger("Иванов", "Петров", "Сидоров")
bus += "Васечкин"
print("Пассажиры в автобусе:", bus.passengers)
print("Свободные места:", bus.available_seats)
print("Занятые места:", bus.seats)

bus.disembark_passenger("Петров")
bus -= "Сидоров"
print("Пассажиры в автобусе:", bus.passengers)
print("Свободные места:", bus.available_seats)
print("Занятые места:", bus.seats)

if "Иванов" in bus:
    print("Иванов в автобусе.")
else:
    print("Иванова нет в автобусе.")


