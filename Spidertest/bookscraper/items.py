# items.py

from scrapy.item import Item, Field

class BookItem(Item):
    title = Field()
    category = Field()
    description = Field()
    price = Field()
