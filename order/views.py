from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet , ModelViewSet
from rest_framework.mixins import CreateModelMixin , RetrieveModelMixin , DestroyModelMixin
from order.models import Cart , CartItem
from order.serializers import CartSerializer , CartItemSerializer , AddCartItemSerializer , UpdateCartItemSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class CartViewSet(CreateModelMixin, RetrieveModelMixin,DestroyModelMixin , GenericViewSet):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)
    

    def get_queryset(self):
        return Cart.objects.filter(user = self.request.user)


class CartItemViewSet(ModelViewSet):

    http_method_names = ['get' , 'post' , 'patch' , 'delete']

    def get_serializer_context(self):
        return {'cart_id' : self.kwargs['cart_pk']}

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart_id = self.kwargs['cart_pk'])