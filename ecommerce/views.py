from django.shortcuts import render
from .models import *
from django.db.models import Count, Avg, Sum, Max, Min
from django.db.models.functions import Round


""" 
F() Expression is used to compare or perform calculations involving the value of one database field with another.

"""

def ecommerce(request):
    # products = Product.objects.all()
    products = Product.objects.annotate(
        total_orders = Count('product_order', distinct=True),
        total_reviews = Count('reviews', distinct=True),
        average_ratings = Avg('reviews__rating', distinct=True, default=0.0),
        total_quantity = Sum('product_order__quantity', distinct=True),
        max_ratings = Max('reviews__rating',  default=0.0),
        min_ratings = Min('reviews__rating',  default=0.0),
    )

    context = {
        'products': products
    }
    return render(request, 'ecommerce.html', context)