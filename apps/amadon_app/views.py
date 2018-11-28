from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Product

# Create your views here.
def home(request):
    return redirect("/amadon")

def index(request):
    context = {
        "all_products": Product.objects.all(),
    }
    if 'count' not in request.session:
        request.session['count'] = 0
    if 'total_spent' not in request.session:
        request.session['total_spent'] = 0

    return render(request, 'amadon_app/index.html', context)

def process(request):
    if request.method == "POST":
        errors = Product.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            print(request.POST)
            this_product = Product.objects.get(id=request.POST['product_id'])
            print(f"Ordered {request.POST['quantity']} of the {this_product.name} for ${this_product.price}")

            request.session['count'] += int(request.POST['quantity'])
            print(f"Session Count = {request.session['count']} items")
            request.session['sum_order'] = int(request.POST['quantity']) * this_product.price
            print(f"Sum of Current Order = ${request.session['sum_order']}")
            request.session['total_spent'] += int(request.POST['quantity']) * this_product.price
            print(f"Session Total Spent = ${request.session['total_spent']}")
            
            return redirect("/amadon/checkout")
    else:
        return redirect("/")

def checkout(request):
    if 'sum_order' not in request.session:
        return redirect("/")
    return render(request, 'amadon_app/checkout.html')