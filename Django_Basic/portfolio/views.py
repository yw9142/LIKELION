from django.shortcuts import render

# Create your views here.
from portfolio.models import Portfolio


def portfolio(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio/portfolio.html', {'portfolios': portfolios})
