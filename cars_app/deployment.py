import os 
from .settings import *
from .settings import BASE_DIR 
import stripe 

#The trusted urls and domains from which requests can come into our applictation 
SECRET_KEY = os.environ['SECRET']
ALLOWED_HOSTS = ['c7-rental-cars-btcpdaf3eqg7czab.uaenorth-01.azurewebsites.net']
CSRF_TRUSTED_ORIGINS = ['https://c7-rental-cars-btcpdaf3eqg7czab.uaenorth-01.azurewebsites.net']

DEBUG = False 


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))#MS ADDED
Temp_Path = os.path.realpath('.')# MS ADDED
index_path =  os.path.join(os.path.dirname(os.path.dirname(__file__)),'templates')


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH ,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATIC_ROOT = os.path.join(BASE_DIR , 'staticfiles')

STATIC_URL = '/static/'
STATICFILES_DIRS=[os.path.join(BASE_DIR , 'staticfiles')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  


MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join(BASE_DIR , 'media')  

connection_string = os.environ.get("AZURE_MYSQL_CONNECTIONSTRING")
parameters = {pair.split("=")[0]: pair.split("=")[1] for pair in connection_string.split(";")}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'c7-rental-cars-database',
        'USER' : 'dybrwudlpi' ,
        'PASSWORD' : 'SAna2679627',
        'HOST' : 'c7-rental-cars-server.mysql.database.azure.com', 
        'PORT' :'3306',
        'OPTIONS': {
            'ssl':{'ssl': True}   
        }
    }
}


#Payment By STRIPE
STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY =os.environ.get('STRIPE_SECRET_KEY')