from .models import Item
from .items import items


class Fruits:
    def __init__(self):
        self.name = []
        self.foriegn_ids = []
    def seperate(self, fruit):
        for key, value in fruit.items():
            self.name.append(key)
            self.foriegn_ids.append(value)
    def generate_items(self):
        for i in self.name:
            # print(i)
            fruit = Item(self.name[i], self.foriegn_ids[i]["name"], self.foriegn_ids[i]["stamina"], self.foriegn_ids[i]["player"], self.foriegn_ids[i]["room"])
            fruit.save()

        
