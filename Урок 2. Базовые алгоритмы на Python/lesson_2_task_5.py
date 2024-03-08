def month_to_season(month_number):
    if month_number in range(1, 3) or month_number == 12:
        return "Зима"
    elif month_number in range(3, 6):
        return "Весна"
    elif month_number in range(6, 9):
        return "Лето"
    elif month_number in range(9, 12):
        return "Осень"
    else:
        return "Неверный номер месяца"


month = 3
season = month_to_season(month)
print(f'Месяц {month} соответствует сезону: {season}')
