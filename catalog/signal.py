from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .serializers import Product, ProductSerializer

@receiver(pre_save, sender=Product, dispatch_uid="update_record")
def update_es_record(sender, instance, **kwargs):
    obj = ProductSerializer(instance)
    obj.save()

@receiver(post_delete, sender=Product, dispatch_uid="delete_record")
def delete_es_record(sender, instance, *args, **kwargs):
    obj = ProductSerializer(instance)
    obj.delete(ignore=404)
