from django.urls import path
from .views import getdata, postdata
urlpatterns = [
    path('', getdata, name="get"),
    path('add', postdata, name='post')
]
