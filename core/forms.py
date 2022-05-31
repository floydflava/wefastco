from django import forms
from .models import BkasPayment
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from allauth.account.forms import SignupForm
from .models import UserProfile,models
from allauth.account.views import PasswordResetView
from django.conf import settings
from django.dispatch import receiver
from django.http import HttpRequest
from django.middleware.csrf import get_token


PAYMENT_CHOICES = (
   
    ('C', 'Cash on delivery (Free Shipping)'),
    ('B', 'Bkash (Free Shipping)'),
    ('S', 'stripe'),
    ('P','paypal')

)




   
class BkasPaymentForm(forms.Form):

    transaction = forms.CharField(max_length=50,widget= forms.TextInput
                           (attrs={'placeholder':'Enter your transaction'}))
    





class CheckoutForm(forms.Form):
    shipping_address = forms.CharField(required=False)
    shipping_address2 = forms.CharField(required=False)
    shipping_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    shipping_zip = forms.CharField(required=False)
    phone_number = forms.CharField(required=False)


    billing_address = forms.CharField(required=False)
    billing_address2 = forms.CharField(required=False)
    billing_country = CountryField(blank_label='(select country)').formfield(
        required=False,
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100',
        }))
    billing_zip = forms.CharField(required=False)


    same_billing_address = forms.BooleanField(required=False)
    set_default_shipping = forms.BooleanField(required=False)
    use_default_shipping = forms.BooleanField(required=False)
    set_default_billing = forms.BooleanField(required=False)
    use_default_billing = forms.BooleanField(required=False)

    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    # phone_number = forms.CharField(max_length=10 )
    # date_of_birth = forms.DateTimeField()
   
    
    def save(self, request):
        UserProfile.user = super(CustomSignupForm, self).save(request)
        UserProfile.user.first_name = self.cleaned_data['first_name']
        UserProfile.user.last_name = self.cleaned_data['last_name']
        # UserProfile.user.phone_number = self.cleaned_data['phone_number']
        # UserProfile.user.date_of_birth = self.cleaned_data['date_of_birth']
        
        
        
        UserProfile.user.save()
        return  UserProfile.user

# @receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
# def send_reset_password_email(sender, instance, created, **kwargs):

#     if created:

#         # First create a post request to pass to the view
#         request = HttpRequest()
#         request.method = 'POST'

#         # add the absolute url to be be included in email
#         if settings.DEBUG:
#             request.META['HTTP_HOST'] = '127.0.0.1:8000'
#         else:
#             request.META['HTTP_HOST'] = 'www.comfiapp.heroku.com'

#         # pass the post form data
#         request.POST = {
#             'email': instance.email,
#             'csrfmiddlewaretoken': get_token(HttpRequest())
#         }
#         PasswordResetView.as_view()(request)  # email will be sent!

class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class RefundForm(forms.Form):
    ref_code = forms.CharField()
    message = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4
    }))
    email = forms.EmailField()


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)

class PaymentFormBkash(forms.Form):
    transaction_id = forms.CharField(required=False)


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')