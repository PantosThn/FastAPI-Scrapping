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
