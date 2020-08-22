from django.urls import path
from . import views
from .views import (
   
    CheckoutView,
    
    OrderSummaryView,
    add_to_cart,
    remove_from_cart,
    remove_single_item_from_cart,
    PaymentView,
    AddCouponView,
    BkashPaymentView,
    OrderSuccessView,
    RequestRefundView
)

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('samsung/', views.samsung, name='samsung'),
    path('xiaomi/', views.xiaomi, name='xiaomi'),
    path('nokia/', views.nokia, name='nokia'),
    path('apple/', views.apple, name='apple'),
    path('realme/', views.realme, name='realme'),
    path('oppo/', views.oppo, name='oppo'),
    path('oneplus/', views.oneplus, name='oneplus'),
    
    path('search/', views.search, name='search'),
    path('confirmed/', views.confirmed, name='confirmed'),
    path('bkash/', views.bkash, name='bkash'),
    
    path('contact/', views.contact, name='contact'),


    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('bkash-payment/', BkashPaymentView.as_view(), name='bkash-payment'),
    path('order-success/', OrderSuccessView.as_view(), name='order-success'),

    path('product/<slug>/', views.product_details, name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart,
         name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund')
]
