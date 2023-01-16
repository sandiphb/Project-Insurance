from django.urls import path
from HR import views

urlpatterns=[
   # path('2/',views.h_fun),
    #path('',views.image),
    path('',views.home),
    path('add/',views.add),
    path('sub/',views.sub),
]