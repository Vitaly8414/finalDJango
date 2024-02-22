from django.core.files.storage import FileSystemStorage
from django.forms import ValidationError
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseServerError
from .models import Client, Product, Order
from .forms import ClientForm, ProductForm, OrderForm
from django.utils import timezone
from datetime import timedelta


def handle_error(request, exception):
    return render(request, "myapp2/error.html", {"exception": exception}, status=500)


# Обработка форм
def handle_form(request, form_class, template_name, redirect_url, instance=None):
    try:
        if request.method == "POST":
            form = form_class(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
                return redirect(redirect_url)
        else:
            form = form_class(instance=instance)
        return render(request, template_name, {"form": form})
    except ValidationError as ve:
        # Обработка неверных данных формы
        return handle_error(request, ve)
    except Exception as e:
        # Обработка других исключений
        return handle_error(request, e)

def base(request):
    return render(request, 'myapp2/base.html')

# Функции для модели Клиент
def client_list(request):
    try:
        clients = Client.objects.all()
        return render(request, "myapp2/client_list.html", {"clients": clients})
    except Exception as e:
        return handle_error(request, e)

def client_detail(request, pk):
    try:
        client = get_object_or_404(Client, pk=pk)
        return render(request, "myapp2/client_detail.html", {"client": client})
    except Exception as e:
        return handle_error(request, e)


def client_create(request):
    return handle_form(request, ClientForm, "myapp2/client_form.html", "myapp_2/client_detail")


def client_edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return handle_form(request, ClientForm, "myapp2/client_form.html", "myapp_2/client_detail", instance=client)


def client_delete(request, pk):
    try:
        client = get_object_or_404(Client, pk=pk)
        client.delete()
        return redirect("myapp2/client_list")
    except Exception as e:
        return handle_error(request, e)


def client_orders(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = client.order_set.all()
    return render(request, "myapp2/client/client_orders.html", {"client": client, "orders": orders})


def client_ordered_products(request, client_id, days):
    client = get_object_or_404(Client, pk=client_id)
    start_date = timezone.now() - timedelta(days=days)
    orders = client.order_set.filter(order_date__gte=start_date)
    ordered_products = set()
    for order in orders:
        ordered_products.update(order.products.all())
    return render(
        request,
        "myapp2/client/client_ordered_products.html",
        {"client": client, "ordered_products": ordered_products, "days": days},
    )


# Функции для модели Товар
def product_list(request):
    try:
        products = Product.objects.all()
        return render(request, "myapp2/product_list.html", {"products": products})
    except Exception as e:
        return handle_error(request, e)


def product_detail(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
        return render(request, "myapp2/product_detail.html", {"product": product})
    except Exception as e:
        return handle_error(request, e)


def product_create(request):
    return handle_form(request, ProductForm, "myapp2/product_form.html", "myapp_2/product_detail")


def add_product(request):
    return handle_form(request, ProductForm, "myapp2/add_product.html", "myapp_2/product_added")


def product_added(request):
    return render(request, "myapp2/product_added.html")


def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return handle_form(request, ProductForm, "myapp2/product_form.html", "myapp_2/product_detail", instance=product)


def product_delete(request, pk):
    try:
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect("myapp2/product_list")
    except Exception as e:
        return handle_error(request, e)


# Функции для модели Заказ
def order_list(request):
    today = timezone.now()
    week_ago = today - timedelta(days=7)
    month_ago = today - timedelta(days=30)
    year_ago = today - timedelta(days=365)

    products_week = Product.objects.filter(order__order_date__gte=week_ago).distinct()
    products_month = Product.objects.filter(order__order_date__gte=month_ago).distinct()
    products_year = Product.objects.filter(order__order_date__gte=year_ago).distinct()

    context = {
        "products_week": products_week,
        "products_month": products_month,
        "products_year": products_year,
    }
    return render(request, "myapp2/orders_list.html", context)


def order_detail(request, pk):
    try:
        order = get_object_or_404(Order, pk=pk)
        return render(request, "myapp2/order_detail.html", {"order": order})
    except Exception as e:
        return handle_error(request, e)


def order_create(request):
    return handle_form(request, OrderForm, "myapp2/order_form.html", "myapp_2/order_detail")


def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return handle_form(request, OrderForm, "myapp2/order_form.html", "myapp_2/order_detail", instance=order)


def order_delete(request, pk):
    try:
        order = get_object_or_404(Order, pk=pk)
        order.delete()
        return redirect("myapp2/orders_list")
    except Exception as e:
        return handle_error(request, e)
