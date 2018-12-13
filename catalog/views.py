# Create your views here.
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.parsers import JSONParser
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrReadOnly
# from django.shortcuts import render
from catalog.products import ProductIndex



class ProductList(generics.ListCreateAPIView):
    """
    GET products/
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly, )

# pass product by ID
class ProductDetail(generics.RetrieveAPIView):
    """
    GET product/:id/
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        try:
            a_product = self.queryset.get(pk=kwargs["pk"])
            return Response(ProductSerializer(a_product).data)
        except Product.DoesNotExist:
            return Response(
            data={
            "message": "Product with id: {} does not exist".format(kwargs["pk"])
            },
            status=status.HTTP_404_NOT_FOUND
            )



class ProductSearch(generics.ListAPIView):
    """
    GET products_search/:?q=<query>
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        query = request.query_params.get('q')
        ids = []
        if query:
            try:
                s = ProductIndex.search()
                s = s.query('match', description=query)
                response = s.execute()
                response_dict = response.to_dict()
                hits = response_dict['hits']['hits']
                ids = [hit['_source']['id'] for hit in hits]
                queryset = Product.objects.filter(id__in=ids)
                product_list = list(queryset)
                product_list.sort(key=lambda product: ids.index(product.id))
                serializer = ProductSerializer(product_list, many=True)
            except Exception as e:
                products = Product.objects.filter(description__icontains=query)
                serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)


#
# class MultipleFieldLookupMixin(object):
#     """
#     Apply this mixin to any view or viewset to get multiple field filtering
#     based on a `lookup_fields` attribute, instead of the default single field filtering.
#     """
#
#     def get_object(self):
#         queryset = self.get_queryset()             # Get the base queryset
#         queryset = self.filter_queryset(queryset)  # Apply any filter backends
#         filter = {}
#         for field in self.lookup_fields:
#             if self.kwargs[field]: # Ignore empty fields.
#                 filter[field] = self.kwargs[field]
#             obj = get_object_or_404(queryset, **filter)  # Lookup the object
#             self.check_object_permissions(self.request, obj)
#             return obj
#
#
# class ProductSearch(MultipleFieldLookupMixin, generics.RetrieveAPIView):
#     """
#     GET products_search/:?q=<query>
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     lookup_fields = ('description', 'code' , 'type')
#
#     def get(self, request):
#         try:
#             a_product = self.queryset.get(lookup_fields)
#             return Response(ProductSerializer(a_product).data)
#         except Product.DoesNotExist:
#             return Response(
#             data={
#             "message": "Product with id: {} does not exist".format(lookup_fields)
#             },
#             status=status.HTTP_404_NOT_FOUND
#             )
