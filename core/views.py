from multiprocessing import context
import random
import string
from unicodedata import category

from requests_toolbelt import user_agent

import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, View
from . import forms,models
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.db.models import Q

from taggit.managers import TaggableManager

from .forms import CheckoutForm, CouponForm, RefundForm, PaymentForm, BkasPaymentForm, ContactForm
from .models import Item, OrderItem, Order, Address, Payment, BkasPayment, Coupon, Refund, UserProfile




def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))


def accessories(request):
    
    items = Item.objects.filter(category='A').order_by('-created_on')
    items_feature_home = Item.objects.all().order_by('-created_on')[:5]

    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    
    context = {

       'items': items,
       'page_obj': page_obj,
       'items_feature_home': items_feature_home
    
    }
    
    return render(request, "accessories.html", context)

def phones(request):
    
    items = Item.objects.filter(category='P').order_by('-created_on')
    items_feature_home = Item.objects.all().order_by('-created_on')[:5]
    
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context = {

       'items': items,
       'page_obj': page_obj,
       'items_feature_home': items_feature_home 
    
    }
    
    return render(request, "phones.html", context)

def exclusive_items(request):
    
    items = Item.objects.filter(category='P').order_by('-created_on')
    items_feature_home = Item.objects.all().order_by('-created_on')[:5]
    
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context = {

       'items': items,
       'page_obj': page_obj,
       'items_feature_home': items_feature_home 
    
    }
    
    return render(request, "exclusive_items.html", context)

def watches(request):
    
    items = Item.objects.filter(category='W').order_by('-created_on')
    items_feature_home = Item.objects.all().order_by('-created_on')[:5]
    
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context = {

       'items': items,
       'page_obj': page_obj,
       'items_feature_home': items_feature_home  
    
    }
    
    return render(request, "watches.html", context)

def laptops(request):
    
    items = Item.objects.filter(category='L').order_by('-created_on')
    items_feature_home = Item.objects.all().order_by('-created_on')[:5]
    
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context = {

       'items': items,
       'page_obj': page_obj,
       'items_feature_home': items_feature_home  
    
    }
    
    return render(request, "laptops.html", context)



def oppo(request):
    
    items = Item.objects.filter(category='Op').order_by('-created_on')
    items_feature_home = Item.objects.all().order_by('-created_on')[:5]
    
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {

       'items': items,
       'page_obj': page_obj,
       'items_feature_home': items_feature_home 
    
    }
    
    return render(request, "oppo.html", context)

def oneplus(request):
    
    items = Item.objects.filter(category='On').order_by('-created_on')
    items_feature_home = Item.objects.filter(category='P').order_by('-created_on')[:8]
    
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {

       'items': items,
       'page_obj': page_obj,
       'items_feature_home': items_feature_home  
    
    }
    
    return render(request, "oneplus.html", context)    


def confirmed(request):

    context = {

       
    
    }
    
    return render(request, "confirmed.html", context)  


def bkash(request):

    
    
    context = {

       
    
    }
    
    return render(request, "bkash.html", context)

def contact_success(request):

    
    
    context = {

       
    
    }
    
    return render(request, "contact_success.html", context)

def order_success(request):

    
    
    context = {

       
    
    }
    
    return render(request, "order_success.html", context)








def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


def home(request):
    
    items = Item.objects.all().order_by('created_on')
    
    items_feature_home = Item.objects.filter(category='A').order_by('-created_on')[:8]
    laptops = Item.objects.filter(category='L').order_by('-created_on')[:8]
    watches_item = Item.objects.filter(category='W').order_by('-created_on')[:8]
    phone_item = Item.objects.filter(category='P').order_by('-created_on')[:8]



    
    
    
    paginator = Paginator(items, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context = {
        'items': items,
        'items_feature_home': items_feature_home,
        'laptops':laptops,
        'watches_item':watches_item,
        'phone_item': phone_item,
        
        
        'page_obj': page_obj
    }
    return render(request, "home.html", context)




def product_details(request, slug):
    
    item = Item.objects.get(slug=slug)
    image_list = item.images.all()
    
    similar_item = item.tags.similar_objects()[:4]
    
    
    context = {

       'item': item,
       'image_list': image_list,
       'similar_item': similar_item

    
    }
    
    return render(request, "product.html", context)


def search(request):
    
    items_feature_home = Item.objects.all().order_by('-created_on')[:5]
    
    
    
    
    queryset = Item.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
           
        
        ).distinct()
    context = {
        'queryset': queryset,
        
        'items_feature_home': items_feature_home 
       

    }
    return render(request, 'search.html', context)



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
           form.save()
           return render(request, 'contact_success.html') # does nothing, just trigger the validation
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)
    
def email_success(request):
    res = 'Email is verified!'
    return HttpResponse('<p>%s</p>' % res)



def is_valid_form(values):
    valid = True
    for field in values:
        if field == '':
            valid = False
    return valid


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            form = CheckoutForm()
            context = {
                'form': form,
                'couponform': CouponForm(),
                'order': order,
                'DISPLAY_COUPON_FORM': True
            }

            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='S',
                default=True
            )
            if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='B',
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("core:checkout")

    def post(self, *args, **kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            if form.is_valid():

                use_default_shipping = form.cleaned_data.get(
                    'use_default_shipping')
                if use_default_shipping:
                    print("Using the defualt shipping address")
                    address_qs = Address.objects.filter(
                        user=self.request.user,
                        address_type='S',
                        default=True
                    )
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shipping_address = shipping_address
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default shipping address available")
                        return redirect('core:checkout')
                else:
                    print("User is entering a new shipping address")
                    shipping_address1 = form.cleaned_data.get(
                        'shipping_address')
                    shipping_address2 = form.cleaned_data.get(
                        'shipping_address2')
                    shipping_country = form.cleaned_data.get(
                        'shipping_country')
                    shipping_zip = form.cleaned_data.get('shipping_zip')
                    phone_number = form.cleaned_data.get('phone_number')


                    if is_valid_form([shipping_address1, shipping_country, shipping_zip,phone_number]):
                        shipping_address = Address(
                            user=self.request.user,
                            street_address=shipping_address1,
                            apartment_address=shipping_address2,
                            country=shipping_country,
                            zip=shipping_zip,
                            phone=phone_number,
                            address_type='S'
                        )
                        shipping_address.save()

                        order.shipping_address = shipping_address
                        order.save()

                        set_default_shipping = form.cleaned_data.get(
                            'set_default_shipping')
                        if set_default_shipping:
                            shipping_address.default = True
                            shipping_address.save()

                    else:
                        messages.info(
                            self.request, "Please fill in the required shipping address fields")

                use_default_billing = form.cleaned_data.get(
                    'use_default_billing')
                same_billing_address = form.cleaned_data.get(
                    'same_billing_address')

                if same_billing_address:
                    billing_address = shipping_address
                    billing_address.pk = None
                    billing_address.save()
                    billing_address.address_type = 'B'
                    billing_address.save()
                    order.billing_address = billing_address
                    order.save()

                elif use_default_billing:
                    print("Using the defualt billing address")
                    address_qs = Address.objects.filter(
                        user=self.request.user,
                        address_type='B',
                        default=True
                    )
                    if address_qs.exists():
                        billing_address = address_qs[0]
                        order.billing_address = billing_address
                        order.save()
                    else:
                        messages.info(
                            self.request, "No default billing address available")
                        return redirect('core:checkout')
                else:
                    print("User is entering a new billing address")
                    billing_address1 = form.cleaned_data.get(
                        'billing_address')
                    billing_address2 = form.cleaned_data.get(
                        'billing_address2')
                    billing_country = form.cleaned_data.get(
                        'billing_country')
                    billing_zip = form.cleaned_data.get('billing_zip')
                    phone_number = form.cleaned_data.get('phone_number')



                    if is_valid_form([billing_address1, billing_country, billing_zip,phone_number]):
                        billing_address = Address(
                            user=self.request.user,
                            street_address=billing_address1,
                            apartment_address=billing_address2,
                            country=billing_country,
                            zip=billing_zip,
                            phone=phone_number,
                            address_type='B'
                        )
                        billing_address.save()

                        order.billing_address = billing_address
                        order.save()

                        set_default_billing = form.cleaned_data.get(
                            'set_default_billing')
                        if set_default_billing:
                            billing_address.default = True
                            billing_address.save()

                    else:
                        messages.info(
                            self.request, "Please fill in the required billing address fields")

                payment_option = form.cleaned_data.get('payment_option')

                if payment_option == 'S':
                    return redirect('core:payment', payment_option='stripe')
                
                elif payment_option == 'P':
                    return redirect('core:payment', payment_option='paypal')
                
                elif payment_option == 'C':
                    return redirect('core:payment', payment_option='cash')

                elif payment_option == 'B':
                    return redirect('core:bkash-payment')
                
                
                else:
                    messages.warning(
                        self.request, "Invalid payment option selected")
                    return redirect('core:checkout')
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("core:order-summary")


class PaymentView(View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        if order.billing_address:
            context = {
                'order': order,
                'DISPLAY_COUPON_FORM': False,
              
            }
            
            payment = Payment()
            payment.user = self.request.user
            payment.amount = order.get_total()
            payment.save()

            # assign the payment to the order

            order_items = order.items.all()
            order_items.update(ordered=True)
            for item in order_items:
                item.ordered = True

                item.itm_code = order.ref_code
                item.save()
            # models.Order.objects.get_or_create(item=order_items, user=self.request.user,ordered=True,status='Pending')

            order.ordered = True
            order.payment = payment
            order.ref_code = create_ref_code()
            order.save()

            messages.success(self.request, "Your order was successful!")
            return redirect("core:order_success")

        
        else:
            messages.warning(
                self.request, "You have not added a billing address")
            return redirect("core:checkout")

    



class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.warning(self.request, "You do not have an active order")
            return redirect("/")


def OrderSuccessView(request):
    orders= Order.objects.all().filter(user=request.user,
        ordered=True).order_by('-ordered_date', 'id')
   

    product_list = []

    for i in orders:
        products = OrderItem.objects.all().filter(itm_code=i, ordered=True )
        product_list.append(products)
   

    context={ 'orders': orders,'products': product_list}
   
    return render(request, "orders.html",context)




class BkashPaymentView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = BkasPaymentForm(self.request.POST)

        if order.billing_address:
            context = {
                'order': order,
                'form': form,
                'DISPLAY_COUPON_FORM': False,
                
            }
            
            return render(self.request, "bkash_payment.html", context)
        else:
            messages.warning(
                self.request, "You have not added a billing address")
            return redirect("core:checkout")

    def post(self, *args, **kwargs):
        order = Order.objects.get(user=self.request.user, ordered=False)
        form = BkasPaymentForm(self.request.POST)
        
        userprofile = UserProfile.objects.get(user=self.request.user)
        
        if form.is_valid():
            
            
            
            
            
            
            try:

                
                # create the payment
                bkaspayment = BkasPayment()
                
                bkaspayment.user = self.request.user
                bkaspayment.transaction = form.cleaned_data['transaction']
                bkaspayment.amount = order.get_total()
                bkaspayment.save()

                # assign the payment to the order

                order_items = order.items.all()
                order_items.update(ordered=True)
                for item in order_items:
                    item.save()

                order.ordered = True
                order.bkash_payment = bkaspayment
                order.ref_code = create_ref_code()
                order.save()

                messages.success(self.request, "Your order was successful!")
                return redirect("core:orders")

            except ObjectDoesNotExist:
                messages.warning(self.request, "You do not have an active order")
                return redirect("/")
            

            

        messages.warning(self.request, "Invalid data received. Submit accurate transactions.")
        return redirect("core:bkash-payment")




@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.item_code = create_ref_code()
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("core:order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:order-summary")


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item quantity was updated.")
            return redirect("core:order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)


def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect("core:checkout")


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)
        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    user=self.request.user, ordered=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect("core:checkout")
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect("core:checkout")


class RequestRefundView(View):
    def get(self, *args, **kwargs):
        form = RefundForm()
        context = {
            'form': form
        }
        return render(self.request, "request_refund.html", context)

    def post(self, *args, **kwargs):
        form = RefundForm(self.request.POST)
        if form.is_valid():
            ref_code = form.cleaned_data.get('ref_code')
            message = form.cleaned_data.get('message')
            email = form.cleaned_data.get('email')
            # edit the order
            try:
                order = Order.objects.get(ref_code=ref_code)
                order.refund_requested = True
                order.save()

                # store the refund
                refund = Refund()
                refund.order = order
                refund.reason = message
                refund.email = email
                refund.save()

                messages.info(self.request, "Your request was received.")
                return redirect("core:request-refund")

            except ObjectDoesNotExist:
                messages.info(self.request, "This order does not exist.")
                return redirect("core:request-refund")
