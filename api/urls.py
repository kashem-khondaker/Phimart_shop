from django.urls import path , include
from product.views import ProductViewSet , CategoryViewSet , ReviewViewSet , ProductImageViewSet
from order.views import CartViewSet , CartItemViewSet , OrderViewSet 
from rest_framework_nested import routers

router =routers.DefaultRouter()
router.register('products' , ProductViewSet , basename='products')
router.register('categories' , CategoryViewSet , basename='categories')
router.register('carts' , CartViewSet , basename='carts')
router.register('orders' , OrderViewSet , basename='orders')

product_router = routers.NestedSimpleRouter(router, r'products', lookup='product')
product_router.register(r'reviews', ReviewViewSet, basename='product-review')
product_router.register('images' , ProductImageViewSet , basename='product-images')

cart_router = routers.NestedDefaultRouter(router , r'carts' , lookup = 'cart')
cart_router.register(r'items' , CartItemViewSet , basename='cart-item')

# urlpatterns = router.urls

urlpatterns = [
    path('' , include(router.urls)),
    path('' , include(product_router.urls)),
    path('' , include(cart_router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
