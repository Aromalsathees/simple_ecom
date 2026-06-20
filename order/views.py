from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from cart.models import Cart
from cart.models import CartItem

from .models import Order
from .models import OrderItem



@login_required
def checkout(request):

    cart = Cart.objects.get(
        user=request.user
    )

    items = cart.items.all()

    total = sum(
        item.subtotal
        for item in items
    )

    context = {
        "items": items,
        "total": total
    }

    return render(
        request,
        "order/checkout.html",
        context
    )

@login_required
def place_order(request):

    cart = Cart.objects.get(
        user=request.user
    )

    items = cart.items.all()

    total = sum(
        item.subtotal
        for item in items
    )

    order = Order.objects.create(

        user=request.user,

        total_amount=total

    )

    for item in items:

        OrderItem.objects.create(

            order=order,

            product=item.product,

            quantity=item.quantity,

            price=item.product.price

        )

    items.delete()

    return redirect(
        "order_history"
    )


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by(
        '-created_at'
    )

    context = {
        "orders": orders
    }

    return render(
        request,
        "order/order_history.html",
        context
    )