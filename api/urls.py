from django.urls import path , include
from product.views import ProductViewSet , CategoryViewSet , ReviewViewSet
from order.views import CartViewSet , CartItemViewSet
from rest_framework_nested import routers

router =routers.DefaultRouter()
router.register('products' , ProductViewSet , basename='products')
router.register('categories' , CategoryViewSet , basename='categories')
router.register('carts' , CartViewSet , basename='carts')

product_router = routers.NestedSimpleRouter(router, r'products', lookup='product')
product_router.register(r'reviews', ReviewViewSet, basename='product-review')
cart_router = routers.NestedDefaultRouter(router , r'carts' , lookup = 'cart')
cart_router.register(r'items' , CartItemViewSet , basename='cart-item')

# urlpatterns = router.urls

urlpatterns = [
    path('' , include(router.urls)),
    path('' , include(product_router.urls)),
    path('' , include(cart_router.urls))
]

# urlpatterns = [
#     path('products/' , include('product.products_urls')),
#     path('categories/' , include('product.categories_urls')),
# ]
