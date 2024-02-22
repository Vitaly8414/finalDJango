"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from myapp2.views import (
    client_list,
    client_detail,
    client_create,
    client_edit,
    client_delete,
    client_orders,
    client_ordered_products,
    product_list,
    product_detail,
    product_create,
    product_edit,
    product_delete,
    add_product,
    product_added,
    order_list,
    order_detail,
    order_create,
    order_edit,
    order_delete,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp2.urls")),
    # path("clients/", client_list, name="client_list"),
    # path("clients/<int:pk>/", client_detail, name="client_detail"),
    # path("clients/create/", client_create, name="client_create"),
    # path("clients/<int:pk>/edit/", client_edit, name="client_edit"),
    # path("clients/<int:pk>/delete/", client_delete, name="client_delete"),
    # path("clients/<int:client_id>/orders/", client_orders, name="client_orders"),
    # path(
    #     "clients/<int:client_id>/ordered-products/<int:days>/",
    #     client_ordered_products,
    #     name="client_ordered_products",
    # ),
    # path("products/", product_list, name="product_list"),
    # path("products/<int:pk>/", product_detail, name="product_detail"),
    # path("products/create/", product_create, name="product_create"),
    # path("products/<int:pk>/edit/", product_edit, name="product_edit"),
    # path("products/<int:pk>/delete/", product_delete, name="product_delete"),
    # path("products/<int:pk>/add_product/", add_product, name="add_product"),
    # path("products/<int:pk>/product_added/", product_added, name="product_added"),
    # path("orders/", order_list, name="order_list"),  
    # path("orders/<int:pk>/", order_detail, name="order_detail"),
    # path("orders/create/", order_create, name="order_create"),
    # path("orders/<int:pk>/edit/", order_edit, name="order_edit"),
    # path("orders/<int:pk>/delete/", order_delete, name="order_delete"),
]
