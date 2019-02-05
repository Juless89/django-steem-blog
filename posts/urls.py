from django.urls import path
from .views import HomePageView, TickerData

urlpatterns = [
    path('', HomePageView.as_view(), kwargs={'account': 'steempytutorials'}, name='home'),
    path('api/ticker/data/', TickerData.as_view()),
    path('@<slug:account>/', HomePageView.as_view(), name='home'),
]
