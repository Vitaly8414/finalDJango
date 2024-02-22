from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('client_list/', views.client_list, name='client_list'),
    # path('client_detail/', views.client_detail, name='client_detail'),
    path("clients/<int:pk>/", views.client_detail, name="client_detail"),
    # path('client_form/', views.client_form, name='client_form'),
    path('client_ordered_products/', views.client_ordered_products, name='client_ordered_products'),
    path('client_orders/', views.client_orders, name='client_orders'),
    path("add_product/", views.add_product, name="add_product"),
    path("product_list/", views.product_list, name="product_list"),
    path("product_added/", views.product_added, name="product_added"),
    path("add_product/", views.add_product, name="add_product"),
    path("product_detail/", views.product_detail, name="product_detail"),
    # path("product_form/", views.product_form, name="product_form"),
    path("order_detail/", views.order_detail, name="order_detail"),
    path("order_list/", views.order_list, name="order_list"),
    # path("order_form/", views.order_form, name="order_form"),
    path("error/", views.handle_error, name="error"),
]

# from django.contrib import admin
# from django.urls import path, include
# from myapp2.views import (
#     client_list,
#     client_detail,
#     client_create,
#     client_edit,
#     client_delete,
#     client_orders,
#     client_ordered_products,
#     product_list,
#     product_detail,
#     product_create,
#     product_edit,
#     product_delete,
#     add_product,
#     product_added,
#     order_list,
#     order_detail,
#     order_create,
#     order_edit,
#     order_delete,
# )

# urlpatterns = [
#     path("clients/", client_list, name="client_list"),
#     path("clients/<int:pk>/", client_detail, name="client_detail"),
#     path("clients/create/", client_create, name="client_create"),
#     path("clients/<int:pk>/edit/", client_edit, name="client_edit"),
#     path("clients/<int:pk>/delete/", client_delete, name="client_delete"),
#     path("clients/<int:client_id>/orders/", client_orders, name="client_orders"),
#     path(
#         "clients/<int:client_id>/ordered-products/<int:days>/",
#         client_ordered_products,
#         name="client_ordered_products",
#     ),
#     path("products/", product_list, name="product_list"),
#     path("products/<int:pk>/", product_detail, name="product_detail"),
#     path("products/create/", product_create, name="product_create"),
#     path("products/<int:pk>/edit/", product_edit, name="product_edit"),
#     path("products/<int:pk>/delete/", product_delete, name="product_delete"),
#     path("products/<int:pk>/add_product/", add_product, name="add_product"),
#     path("products/<int:pk>/product_added/", product_added, name="product_added"),
#     path("orders/", order_list, name="order_list"),  
#     path("orders/<int:pk>/", order_detail, name="order_detail"),
#     path("orders/create/", order_create, name="order_create"),
#     path("orders/<int:pk>/edit/", order_edit, name="order_edit"),
#     path("orders/<int:pk>/delete/", order_delete, name="order_delete"),
# ]