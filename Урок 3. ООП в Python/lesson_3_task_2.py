from smartphone import Smartphone

catalog = [
    Smartphone("Vivo", "X100 Ultra", "+79555222555"),
    Smartphone("Oppo", "Find X7 Ultra", "+79111000111"),
    Smartphone("Samsung", "Galaxy S23 Ultra", "+79123456789"),
    Smartphone("Huawei", "Pura 70 Ultra", "+79777888999"),
    Smartphone("Apple", "iPhone 15 Pro", "+79987654321")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
