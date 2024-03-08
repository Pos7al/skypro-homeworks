side_of_the_square = input("Введите сторону квадрата: ")

# Заменяем запятую на точку, если пользователь ввел дробное число с запятой:
side_of_the_square = side_of_the_square.replace(',', '.')

side = float(side_of_the_square)


def square(side):
    return side ** 2 if side % 1 == 0 else int(side + 1) ** 2


square_area = square(side)

print(f'Площадь квадрата со стороной {side_of_the_square} равна {square_area}')
