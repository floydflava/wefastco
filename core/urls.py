from django.urls import path
from . import views
from .views import (
   
    CheckoutView,
    OrderSummaryView,
    OrderSuccessView,
   
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    
    PaymentView,
    AddCouponView,
    BkashPaymentView,
   
    RequestRefundView
)

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('accessories/', views.accessories, name='accessories'),
    path('phones/', views.phones, name='phones'),
    path('exclusive_items/', views.exclusive_items, name='exclusive_items'),

    path('watches/', views.watches, name='watches'),
    path('laptops/', views.laptops, name='laptops'),
   
    path('oppo/', views.oppo, name='oppo'),
    path('oneplus/', views.oneplus, name='oneplus'),
    
    path('search/', views.search, name='search'),
    path('bkash/', views.bkash, name='bkash'),
    
    path('contact/', views.contact, name='contact'),
    path('contact_success/', views.contact_success, name='contact_success'),
    path('order_success/', views.order_success, name='order_success'),
    


    path('orders-success/', views.OrderSuccessView, name='orders-success'),
    path('email_success/', views.email_success, 
    name='email_success'),



    path('checkout/', CheckoutView.as_view(), name='checkout'),
  
    path('bkash-payment/', BkashPaymentView.as_view(), name='bkash-payment'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),


    path('product/<slug>/', views.product_details, name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
