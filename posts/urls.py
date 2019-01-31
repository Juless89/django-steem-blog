from django.urls import path
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), kwargs={'account': 'steempytutorials'}, name='home'),
    path('@<slug:account>/', HomePageView.as_view(), name='home')
]
