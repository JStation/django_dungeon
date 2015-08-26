from django.shortcuts import render, redirect
from dungeon.forms import NewAdventureForm

def home_page(request):
    return render(request, 'home.html')

def new_adventure(request):
    if request.method == 'POST':
        form = NewAdventureForm(request.POST)
        if form.is_valid():
            adventure_ = form.save()
            return redirect(adventure_)
    else:
        form = NewAdventureForm()

    return render(request, 'new_adventure.html', {'form': form})


def edit_adventure(request, adventure_id):

    return render(request, 'edit_adventure.html', {'adventure_id':adventure_id})
