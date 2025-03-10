from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product , Category
from product.serializers import ProductSerializers , CategorySerializers
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin , ListModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.



class ProductListCreateView(ListCreateAPIView):
    queryset = Product.objects.select_related('category').all() # product list dekanor jonno ki queryset dorkar saita dite hobe 
    serializer_class = ProductSerializers # kon serializer babohar kortesi saita bolar jonno serializer_class attribute ka override korte hobe .. 

    # def get_queryset(self):
    #     return Product.objects.select_related('category').all()
    
    # def get_serializer_class(self):
    #     return ProductSerializers
    
    # def get_serializer_context(self):
    #     return {'request' : self.request}


class ProductListCreateUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'

    # def delete(self , request , pk):
    #     product = get_object_or_404(Product , pk=pk)
    #     if product.quantity > 10 :
    #         return Response({'message':'you cannot delete more than 10 product at a time . '})
    #     product.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)





class CategoriesCreateViewList(ListCreateAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializers


class CategoryCreateViewUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_count=Count('products')).all()
    serializer_class = CategorySerializers
    lookup_field = 'pk'









"""
@api_view(['GET' , 'POST'])
def view_products(request):
    if request.method == 'GET':
        product = Product.objects.select_related('category').all()
        serializer = ProductSerializers(product , many = True , context={'request': request}) # onek golo product ka pass korle many= True dite hobe 
        return Response(serializer.data)
    if request.method =='POST':
        serializer = ProductSerializers(
            data = request.data , 
            # context={'request': request}
        ) # deserializer proses
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
"""

"""
class ViewProducts(APIView):
    def get(self , request):
        product = Product.objects.select_related('category').all()
        serializer = ProductSerializers(product , many = True , context={'request': request}) # onek golo product ka pass korle many= True dite hobe 
        return Response(serializer.data)

    def post(self , request):
        serializer = ProductSerializers(
            data = request.data , 
            # context={'request': request}
        ) # deserializer proses
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
"""


"""
class ViewSpecificProducts(APIView):
    def get(self , request , pk):
        product = get_object_or_404(Product, pk = pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)

    def put(self , request , pk):
        product = get_object_or_404(Product , pk = pk)
        serializer = ProductSerializers(product , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    
    def delete(self , request , pk):
        product = get_object_or_404(Product , pk = pk)
        copy_product = ProductSerializers(product)
        product.delete()
        return Response(copy_product.data , status=status.HTTP_204_NO_CONTENT)
"""

"""

class ViewCategories(APIView):

    def get(self , request):
        category = Category.objects.annotate(product_count=Count('products'))
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

    def post(self , request):
        serializer = CategorySerializers(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()

            category = Category.objects.annotate(product_count=Count('products')).get(id=instance.id)

            response_serializer = CategorySerializers(category)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""


"""
@api_view(['GET' , 'PUT' , 'DELETE'])
def view_specific_products(request , pk):
    
    
    
    product_dict = {
        "id": product.id,
        "name": product.name,
        "price": product.price
    }
    
    if request.method == 'GET':
        product = get_object_or_404(Product, pk = pk)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    if request.method == 'PUT':
        product = get_object_or_404(Product , pk = pk)
        serializer = ProductSerializers(product , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        product = get_object_or_404(Product , pk = pk)
        copy_product = ProductSerializers(product)
        product.delete()
        return Response(copy_product.data , status=status.HTTP_204_NO_CONTENT)
"""

"""
@api_view(['GET', 'POST'])
def view_categories(request):

    if request.method == 'GET':
        category = Category.objects.annotate(product_count=Count('products')).all()
        serializer = CategorySerializers(category, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = CategorySerializers(data=request.data)

        if serializer.is_valid():
            instance = serializer.save()

            if instance is None:
                return Response({"error": "Failed to create category"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            category = Category.objects.annotate(product_count=Count('products')).get(id=instance.id)

            response_serializer = CategorySerializers(category)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

"""
@api_view(['GET' , 'PUT' , 'DELETE'])
def view_specific_category(request , pk):
    if request.method == 'GET':
        category = get_object_or_404(Category, pk=pk)
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    if request.method == 'PUT':
        category = get_object_or_404(Category , pk=pk)
        serializer = CategorySerializers(category , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        category = get_object_or_404(Category , pk = pk)
        copy_category = category
        category.delete()
        copy_category = CategorySerializers(copy_category )
        return Response(copy_category.data , status=status.HTTP_204_NO_CONTENT)
"""


"""
class ViewSpecificCategory(APIView):

    def get(self , request , pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')).all(), 
            pk=pk
        )
        serializer = CategorySerializers(category)
        return Response(serializer.data)
    
    def put(self , request , pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')).all(),
            pk=pk
        )
        serializer = CategorySerializers(category , data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def delete(self , request , pk):
        category = get_object_or_404(
            Category.objects.annotate(product_count=Count('products')).all() , 
            pk = pk
        )
        copy_category = category
        category.delete()
        copy_category = CategorySerializers(copy_category )
        return Response(copy_category.data , status=status.HTTP_204_NO_CONTENT)
"""