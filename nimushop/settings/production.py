from .base import *
from decouple import config
import django_heroku
import dj_database_url

DEBUG = True  


ALLOWED_HOSTS = ['paukau.herokuapp.com',"wefast.co.za"]
# ALLOWED_HOSTS = ['*']

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]

cloudinary.config( 
  cloud_name = "heaffbctn", 
  api_key = "511192353119356", 
  api_secret = "yrkrMDXEkGyvRG670e1s5Fdnv2U" 
)

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'



DATABASES = {
    'default': dj_database_url.config()
        
    }
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'


django_heroku.settings(locals())