from address import Address
from mailing import Mailing

to_address = Address("987654", "Москва", "Весёлый бульвар", "12", "4")
from_address = Address("456789", "Санкт-Петербург", "Проспект Героев", "3", "4")

mailing = Mailing(to_address, from_address, 750, "TRKNR9898989898RU")

print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, "
      f"{mailing.from_address.city}, {mailing.from_address.street}, "
      f"{mailing.from_address.house} - {mailing.from_address.apartment} "
      f"в {mailing.to_address.postal_code}, {mailing.to_address.city}, "
      f"{mailing.to_address.street}, {mailing.to_address.house} "
      f"-{mailing.to_address.apartment}. "
      f"Стоимость {mailing.cost} рублей.")
