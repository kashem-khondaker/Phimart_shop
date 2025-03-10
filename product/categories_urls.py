from django.urls import path , include
from product import views

urlpatterns = [
    path('' , views.CategoriesCreateViewList.as_view() , name="category_list"),
    path('<int:pk>/' , views.CategoryCreateViewUpdateDestroy.as_view() , name='view_specific_category'),
    # path('' , views.ViewCategories.as_view() , name="category_list"),
    # path('' , views.view_categories , name="category_list"),
    # path('<int:pk>/' , views.view_specific_category , name='view_specific_category'),
]