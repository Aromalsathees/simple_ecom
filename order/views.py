from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required

from django.conf import settings

from cart.models import Cart

from .models import Order
from .models import OrderItem

import razorpay


@login_required
def checkout(request):

    cart = Cart.objects.get(user=request.user)

    items = cart.items.all()

    total = sum(item.subtotal for item in items)

    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    payment = client.order.create({
        "amount": int(total * 100),
        "currency": "INR",
        "payment_capture": 1
    })

    request.session["razorpay_order_id"] = payment["id"]

    context = {
        "items": items,
        "total": total,
        "payment": payment,
        "key": settings.RAZORPAY_KEY_ID
    }

    return render(request, "order/checkout.html", context)


@login_required
def payment_success(request):

    payment_id = request.GET.get("payment_id")

    razorpay_order_id = request.session.get(
        "razorpay_order_id"
    )

    cart = Cart.objects.get(user=request.user)

    items = cart.items.all()

    total = sum(item.subtotal for item in items)

    order = Order.objects.create(
        user=request.user,
        total_amount=total,
        is_paid=True,
        razorpay_order_id=razorpay_order_id,
        razorpay_payment_id=payment_id
    )

    for item in items:

        OrderItem.objects.create(
            order=order,
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    items.delete()

    return redirect("order_history")


@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by("-created_at")

    context = {
        "orders": orders
    }

    return render(
        request,
        "order/order_history.html",
        context
    )