from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model
data = {
    "asin": "AMZNIDNUMBERd",
    "title": "Mark 1adsf"
}


class Product(Model): # -> table
    __keyspace__ = "scrapper_app" #
    asin = columns.Text(primary_key=True, required=True)
    title = columns.Text()

class ProductScrapeEvent(Model):
    __keyspace__ = "scrapper_app"
    uuid = columns.UUID(primary_key=True)
    asin = columns.Text(index=True)
    title = columns.Text()
    price_str = columns.Text(default="-100")