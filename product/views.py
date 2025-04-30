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
from api.permissions import IsAdminOrReadOnly
from drf_yasg.utils import swagger_auto_schema

# Create your views here.



class ProductViewSet(ModelViewSet):
    """
    Product API endpoint description :
     - Allow all user to show product data .
     - Allow authenticated user to show data .
     - Every user can brows search and filter product .
     - Support searching by name and description
     - Support ordering by price and category
    """
    # queryset = Product.objects.all()
    serializer_class = ProductSerializers

    filter_backends = [DjangoFilterBackend , SearchFilter , OrderingFilter]
    filterset_class = ProductFilterSet
    pagination_class = DefaultPagination
    search_fields = ['name' , 'description' ] 
    ordering_fields = ['price' , 'updated_at']
    permission_classes = [FullDjangoModelPermission]

    def get_queryset(self):
        return Product.objects.prefetch_related('images').all()

    def list(self, request, *args, **kwargs):
        """Retrive all the products ."""
        return super().list(request, *args, **kwargs)
    
    @swagger_auto_schema(
            operation_summary = "create a product by admin",
            operation_description="this allow to only admin .",
            request_body=ProductSerializers,
            responses={
                201:ProductSerializers,
                400: "Bad Request . "
            }
    )
    def create(self, request, *args, **kwargs):
        """Only authenticated admin can create product ."""
        return super().create(request, *args, **kwargs)


class ProductImageViewSet(ModelViewSet):
    serializer_class = ProductImageSerializer
    permission_classes = [IsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(product_id = self.kwargs.get('product_pk'))

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return ProductImage.objects.none()
        return ProductImage.objects.filter(product_id = self.kwargs['product_pk'])


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializers
    lookup_field = 'pk'
    # permission_classes = IsAdminOrReadOnly
    permission_classes = [IsAdminOrReadOnly]



class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsReviewAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user = self.request.user)

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Review.objects.none()
        return Review.objects.filter(product_id = self.kwargs.get('product_pk'))

    def get_serializer_context(self):
        return {'product_id': self.kwargs.get('product_pk')}