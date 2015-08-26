from django.shortcuts import render, HttpResponseRedirect
from dungeon.forms import NewAdventureForm

def home_page(request):
    return render(request, 'home.html')

def new_adventure(request):
    if request.method == 'POST':
        form = NewAdventureForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/edit/')
    else:
        form = NewAdventureForm()

    return render(request, 'new_adventure.html', {'form': form})


def edit_adventure(request):

    return render(request, 'edit_adventure.html')
