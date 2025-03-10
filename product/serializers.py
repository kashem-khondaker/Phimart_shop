from rest_framework import serializers
from decimal import Decimal
from product.models import Category , Product



class CategorySerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id' , 'name' , 'description' , 'product_count']

    product_count = serializers.IntegerField( read_only = True)


    # product_count = serializers.SerializerMethodField(method_name='get_product_count')

    # def get_product_count(self , category):
    #     count = Product.objects.filter(category= category).count()
    #     return count



class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'  to display all property 
        fields = ['id' , 'name' , 'price' , 'stock' , 'category' , 'price_with_tax']
    
    price_with_tax = serializers.SerializerMethodField( method_name='calculate_tax')
    # category = serializers.HyperlinkedRelatedField(
    #     queryset = Category.objects.all(),
    #     view_name = 'view_specific_category'
    # ) hyperlink add korte chaile amon vabe dite hobe 
    def calculate_tax(self , product):
        return round(product.price * Decimal(1.1) , 2)
    
    # field level validation ----
    def validate_price(self , price):
        if price < 0:
            raise serializers.ValidationError('price could not be negative !')
        return price 
    

"""
class CategorySerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
"""

"""
class ProductSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    Unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')

    price_with_tax = serializers.SerializerMethodField( method_name='calculate_tax')
    
    # category = serializers.PrimaryKeyRelatedField(
    #     queryset = Category.objects.all()
    # )
    
    # category = serializers.StringRelatedField()
    
    # category = CategorySerializers() # jodi ami nested vabe dite chai tahole ai vabe dite hobe 
    
    category = serializers.HyperlinkedRelatedField(
        queryset = Category.objects.all(),
        view_name = 'view_specific_category'
    )

    def calculate_tax(self , product):
        return round(product.price * Decimal(1.1) , 2)
"""