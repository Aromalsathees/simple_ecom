from django.urls import path
from .views import *

urlpatterns = [

    path("checkout/",checkout, name="checkout"),
    path("history/",order_history,name="order_history"),
    path("payment-success/",payment_success,name="payment_success"),

]

