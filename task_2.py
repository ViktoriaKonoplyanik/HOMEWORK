def days_to_save_money(N, k):
    saved_money = 0
    days = 0

    for day in range(1, k+1):
        if day % 7 != 0:
            saved_money += k
            if saved_money >= N:
                return day

N = int(input("Введите стоимость телефона: "))
k = int(input("Введите сумму, которую Маша может копить каждый день: "))

days_needed = days_to_save_money(N, k)
print(f"Маша накопит необходимую сумму через {days_needed} дней.")