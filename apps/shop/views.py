from django.shortcuts import render
from django.views import View

from apps.shop.models import Product

# Create your views here.
class HomeView(View):
    def get(self, request):
        products = Product.objects.all()[:6]
        context = {"products": products}
        return render(request, "shop/home.html", context)