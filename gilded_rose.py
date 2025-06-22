# -*- coding: utf-8 -*-
from items_business_logic import ConjuredItemLogic 
class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        # initializing conjured item object here instead of inside loop to avoid instance creation multiple times unnecessarily.
        conjured = ConjuredItemLogic()
        for item in self.items:
            """
            Adding conjured item logic using a separate class . The same way can be used for other items
            with specific business logic.
            """
            if "conjured" in item.name.lower():
                print("#"*30)
                print(f"Processing conjured item: {item.name}") 
                conjured.items_operation(item)      
                print(f"Updated conjured item: {item.name}, Sell In: {item.sell_in}, Quality: {item.quality}")
                print("#"*30)
            # end of conjured item logic hrerr        
            elif item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
