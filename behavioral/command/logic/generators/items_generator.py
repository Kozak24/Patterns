from random import choice, randint
from typing import List

from behavioral.command.data import Item


class ItemsGenerator:
    __NAMES = ["Idzuna", "Zendos", "Mankeru", "Kinkaru", "Kokeshitsu", "Nanba", "West", "Cotton", "Wooden", "Stolen"]
    __TYPES = ["Necklace", "Gloves", "Shoes", "Coat", "Pants", "Hat"]

    def generate_items(self, items_amount: int) -> List[Item]:
        items = list()
        for _ in range(0, items_amount):
            item = self.generate_item()

            items.append(item)

        return items

    def generate_item(self) -> Item:
        item_name = choice(self.__NAMES)
        item_type = choice(self.__TYPES)
        item_full_name = f"{item_name} {item_type}"
        item_name_length = len(item_full_name)
        price = randint(item_name_length * 2, item_name_length * 5)

        item = Item(item_full_name, price)

        return item
