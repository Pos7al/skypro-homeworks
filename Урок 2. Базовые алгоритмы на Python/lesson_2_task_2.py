# Шаг 2:
is_year_leap = input("Введите год: ")  # str
input_year = int(is_year_leap)  # int

if input_year % 4 == 0:
    print(True)
else:
    print(False)


# Шаги 3, 4, 5:
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


result = is_year_leap(2024)

print(f"год 2024: {result}")
