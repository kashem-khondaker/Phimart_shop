from django.urls import path , include
from product.views import ProductViewSet , CategoryViewSet , ReviewViewSet
from rest_framework_nested import routers

router =routers.DefaultRouter()
router.register('products' , ProductViewSet , basename='products')
router.register('categories' , CategoryViewSet)

product_router = routers.NestedSimpleRouter(router, r'products', lookup='product')
product_router.register(r'reviews', ReviewViewSet, basename='product-review')

# urlpatterns = router.urls

urlpatterns = [
    path('' , include(router.urls)),
    path('' , include(product_router.urls)),
]

# urlpatterns = [
#     path('products/' , include('product.products_urls')),
#     path('categories/' , include('product.categories_urls')),
# ]
