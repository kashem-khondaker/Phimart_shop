from django.shortcuts import render , get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product , Category , Review
from product.serializers import ProductSerializers , CategorySerializers ,ReviewSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilterSet
from rest_framework.filters import SearchFilter , OrderingFilter
from product.paginations import DefaultPagination
# Create your views here.



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = ProductFilterSet
    pagination_class = DefaultPagination
    search_fields = ['name' , 'description' ] # 'category__name'
    ordering_fields = ['price' , 'updated_at']


    def destroy(self , request , *args , **kwargs ):
        product = self.get_object()
        if product.stock > 10 :
            return Response({'message':'you cannot delete more than 10 product at a time . '})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializers
    lookup_field = 'pk'



class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id' : self.kwargs['product_pk']}