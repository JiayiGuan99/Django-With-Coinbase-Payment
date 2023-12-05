from django.shortcuts import render
from coinbase_commerce.client import Client
from core import settings

def home_view(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Subscription',
        'description': 'Unlimited queries.',
        'local_price': {
            'amount': '10.99',
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
    }
    charge = client.charge.create(**product)

    return render(request, 'home.html', {
        'charge': charge,
    })
    
def success_view(request):
    return render(request, 'success.html', {})


def cancel_view(request):
    return render(request, 'cancel.html', {})