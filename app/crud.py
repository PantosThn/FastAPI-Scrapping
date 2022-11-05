import uuid
from cassandra.cqlengine.management import sync_table
from .db import get_session
from .models import Product, ProductScrapeEvent

session = get_session()
sync_table(Product)
sync_table(ProductScrapeEvent)

def create_entry(data:dict):
    return Product.create(**data)

def create_scrape_entry(data:dict):
    data['uuid'] = uuid.uuid1() # includes a timestamp
    return ProductScrapeEvent.create(**data)

def add_scrape_event(data:dict, fresh=False):
    product = create_entry(data)
    scrape_ojb = create_scrape_entry(data)
    return product, scrape_ojb