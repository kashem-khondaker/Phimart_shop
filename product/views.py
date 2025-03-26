from django.shortcuts import render , get_object_or_404
from rest_framework.decorators import api_view
from product.models import Product , Category , Review , ProductImage
from product.serializers import ProductSerializers , CategorySerializers ,ReviewSerializer , ProductImageSerializer
from django.db.models import Count
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from product.filters import ProductFilterSet
from rest_framework.filters import SearchFilter , OrderingFilter
from product.paginations import DefaultPagination
from rest_framework.permissions import DjangoModelPermissions
from product.permissions import FullDjangoModelPermission , IsReviewAuthorOrReadOnly
# Create your views here.



class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = ProductFilterSet
    pagination_class = DefaultPagination
    search_fields = ['name' , 'description' ] 
    ordering_fields = ['price' , 'updated_at']
    permission_classes = [FullDjangoModelPermission]


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer

    def perform_create(self, serializer):
        serializer.save(product_id = self.kwargs['product_pk'])

    def get_queryset(self):
        return ProductImage.objects.filter(product_id = self.kwargs['product_pk'])


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializers
    lookup_field = 'pk'
    # permission_classes = IsAdminOrReadOnly
    permission_classes = [DjangoModelPermissions]



class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        return Review.objects.filter(product_id = self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id' : self.kwargs['product_pk']}