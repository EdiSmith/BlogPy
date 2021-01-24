from django.urls import path
from .views import IndexPage, ContactPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('contact/', ContactPage.as_view(), name='contact'),
]
