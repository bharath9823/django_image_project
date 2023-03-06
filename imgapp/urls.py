from django.urls import path
from imgapp import views

urlpatterns=[
    path('',views.display)
]