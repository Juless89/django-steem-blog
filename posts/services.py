from beem.blockchain import Blockchain
from beem.account import Account
from beem.comment import Comment
from beem.exceptions import ContentDoesNotExistsException
from beem import Steem

import re, requests, json

# retrieve account blog history
def account_history(username):
    stm = Steem("https://steemd.minnowsupportproject.org")
    account = Account(username, steem_instance=stm)
            
    data = account.blog_history(limit=9, reblogs=False)
    return_data = []

    # try to find the first url for the thumbnail image
    for blog in data:
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[./\-%]|[!*,]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', blog.body) 
        return_data.append([blog, ('https://steemitimages.com/640x480/' + url[0])])

    return return_data

# Get request for coinmarketcap, returns a string of the current price
def get_market_price(token):
    api_url = 'https://api.coinmarketcap.com/v1/ticker/{}/'.format(token)
    response = requests.get(api_url)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))[0]['price_usd']
    else:
        return None