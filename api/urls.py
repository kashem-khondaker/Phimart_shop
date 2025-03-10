from django.urls import path , include

urlpatterns = [
    path('products/' , include('product.products_urls')),
    path('categories/' , include('product.categories_urls')),
]
