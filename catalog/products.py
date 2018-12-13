from elasticsearch_dsl import DocType, Text, Integer, Completion, analyzer, tokenizer
from django_elasticsearch_dsl import DocType, Index,fields, Text
from .models import Product


# Name of the Elasticsearch index
products = Index('products')


@products.doc_type
class ProductIndex(DocType):

    class Meta:
        model = Product
        fields = [
        'type','category','code','ven', 'hfr','description','uom','price'
        ]
        index = 'product'

        # Add indexing method
    def indexing(self):
        obj = ProductIndex(
        meta={
            'id': self.id,
            'type' : self.type,
            'category' : self.category,
            'code' : self.code,
            'ven' : self.ven,
            'hfr' : self.hfr,
            'description' : self.description,
            'uom' : self.uom,
            'price' : self.price
            }
        )
        obj.save()
        return obj.to_dict(include_meta=True)
