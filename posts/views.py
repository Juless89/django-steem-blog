from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.http import HttpResponseNotFound
from .services import account_history
from beem.exceptions import AccountDoesNotExistsException


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