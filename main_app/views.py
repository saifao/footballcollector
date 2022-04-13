from django.shortcuts import render
from .models import Player

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def football_index(request):
    footballers = Player.objects.all()
    return render(request, 'football/index.html', {'footballers': footballers})

def player_detail(request, player_id):
    footballer = Player.objects.get(id=player_id)
    return render(request, 'football/detail.html', {'player': footballer})