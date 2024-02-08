from django.urls import path
from .views import showdata

urlpatterns = [
    # path('', table,name="table"),
    path("",showdata,name="show")
]