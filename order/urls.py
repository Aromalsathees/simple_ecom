from django.urls import path
from .views import *

urlpatterns = [

    path(
        "checkout/",
        checkout,
        name="checkout"
    ),

    path(
        "place/",
        place_order,
        name="place_order"
    ),

    path(
        "history/",
        order_history,
        name="order_history"
    ),

]