from django.shortcuts import render

def index(request):
    return render(request, 'name/index.html')

def dashboard(request):
    return render(request, 'name/dashboard.html')

def analytics(request):
    return render(request, 'name/analytics.html')

def newsline(request):
    return render(request, 'name/newsline.html')

def news(request):
    return render(request, 'name/news.html')

def account(request):
    return render(request, 'name/account.html')

def wallet(request):
    return render(request, 'name/wallet.html')

def catalogue(request):
    return render(request, 'name/catalogue.html')

def review(request):
    return render(request, 'name/review.html')

def catalogue2(request):
    return render(request, 'name/catalogue2.html')