from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.generic import ListView
from django.http import HttpResponseNotFound
from .services import account_history, get_market_price
from beem.exceptions import AccountDoesNotExistsException
from rest_framework.views import APIView
from rest_framework.response import Response


# View for the homepage that will display blog posts of the author
# in a list.
class HomePageView(ListView):
    template_name = 'album.html'
    context_object_name = 'all_posts_list'

    # Try to get blog posts from account, if the account does exist
    # return not found. Override the queryset with the obtained data.
    def get(self, request, *args, **kwargs):
        try:
            self.queryset = account_history(kwargs['account'])
        except AccountDoesNotExistsException:
            print('Account does not exist')
            return HttpResponseNotFound("Invalid account")   

        # Use the original function to generate the html reponse.
        return super().get(request, *args, **kwargs)


# APIview for coinmarketcap STEEM and SBD ticker prices.
class TickerData(APIView):
    # Unused user authentication classes
    authentication_classes = []
    permission_classes = []
    
    # Retrieve STEEM and SBD market prices, return a dict
    def get(self, request, format=None):
        data = {
            "STEEM": '{:.3f}'.format(float(get_market_price('steem'))),
            "SBD": '{:.3f}'.format(float(get_market_price('steem-dollars'))),
        }

        return Response(data)