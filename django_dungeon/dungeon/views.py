from django.shortcuts import render


def home_page(request):
    return render(request, 'home.html')

def new_adventure(request):
    return render(request, 'new_adventure.html')
