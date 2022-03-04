from django.urls import path
from base.views import home_view
urlpatterns = [
    path('session', home_view, name='home'),
]
