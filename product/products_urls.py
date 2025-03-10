from django.urls import path , include
from product import views

urlpatterns = [
    path('',views.ProductListCreateView.as_view() , name='product_list'),
    path('<int:pk>/' , views.ProductListCreateUpdateDestroy.as_view() , name='view_specific_products'),
    # path('',views.ViewProducts.as_view() , name='product_list'),
    # path('',views.view_products.as_view() , name='product_list'),
    # path('<int:pk>/' , views.view_specific_products , name='view_specific_products'),
]