from django.apps import AppConfig
from elasticsearch_dsl import connections
from django.conf import settings


class CatalogConfig(AppConfig):
    name = 'catalog'

    def ready(self):
        import catalog.signals
        try:
          connections.create_connection(
              'product',
              hosts=[{'host': settings.ES_HOST, 'port': settings.ES_PORT}])
        except Exception as e:
          print(e)
