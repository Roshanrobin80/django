from django.urls import path
from . import views


urlpatterns=[
    path('',views.demo),
    path('dem1/<int:a>',views.demo1),
    path('bonus/<int:a>/<int:b>',views.bonus),
    path('monument/<a>',views.monument),
    path('div/<int:a>',views.div),
    path('day/<int:a>',views.day),
    path('tax/<int:a>',views.tax),
    path('elec/<int:a>',views.elec),
    path('demo',views.demo)


]