def bank(x, y):
    deposit_amount = x
    for i in range(y):
        deposit_amount += deposit_amount * 0.10
    return deposit_amount


x = 2000
y = 5

final_balance = bank(x, y)

print(f"Спустя срок (в годах): {y}\n"
      f"На счету пользователя будет сумма: {final_balance}")
