from django.urls import path

from .views import get_featuring_view, home_view


urlpatterns = [
    path('get_featuring', get_featuring_view, name='get_featuring'),
    path('', home_view, name='home')
]
