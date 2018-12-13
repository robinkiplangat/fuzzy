import time
import os
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from elasticsearch_dsl import Search, Index, connections
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from .models import Product
from products import ProductIndex

class Command(BaseCommand):
    help = 'Indexes Products in Elastic Search'
    def handle(self, *args, **options):
        es = Elasticsearch(
            [{'host': settings.ES_HOST, 'port': settings.ES_PORT}],
            index="product"
        )
        product_index = Index('product', using='description')
        product_index.doc_type(ProductIndex)
        if product_index.exists():
            product_index.delete()
            print('Deleted product index.')
        ProductDoc.init()
        result = bulk(
            client=es,
            actions=(product.indexing() for product in product.objects.all().iterator())
        )
        print('Indexed products.')
        print(result)
