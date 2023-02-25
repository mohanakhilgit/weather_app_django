from django.urls import path
from .views import home


app_name = 'website'

urlpatterns = [
    path('', home, name='home'),
    ]
    