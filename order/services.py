from order.models import Cart , CartItem , Order , OrderItem
from django.db import transaction

class OrderServices:
    @staticmethod
    def create_order(user_id , cart_id):
        with transaction.atomic():
            
            cart = Cart.objects.get(pk=cart_id)
            cart_items = CartItem.objects.filter(cart=cart).select_related('product')

            # অর্ডারের মোট দাম হিসাব করছি
            total_price = sum([item.product.price * item.quantity for item in cart_items])

            # নতুন অর্ডার তৈরি করছি
            order = Order.objects.create(
                user_id=user_id,
                total_price=total_price
            )

            # OrderItem গুলো তৈরি করা
            order_items = [
                OrderItem(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price,
                    total_price=item.product.price * item.quantity
                ) for item in cart_items
            ]
            OrderItem.objects.bulk_create(order_items)

            # কার্ট এবং কার্ট আইটেমস ডিলিট করছি
            cart_items.delete()
            cart.delete()

            return order