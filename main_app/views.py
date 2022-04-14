from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
from .forms import WageForm

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
    wage_form = WageForm()
    return render(request, 'football/detail.html', {'player': footballer, 'wage_form': wage_form})

def add_wage(request, player_id):
    wage_form = WageForm(request.POST)
    if wage_form.is_valid():
        new_paystub = wage_form.save(commit=False)
        new_paystub.player_id = player_id
        new_paystub.save()
    return redirect('player', player_id=player_id)

class EnterPlayer(CreateView):
    model=Player
    fields='__all__'

class UpdatePlayer(UpdateView):
    model=Player
    fields=['age','position','mkt_value', 'contract_exp']

class DeletePlayer(DeleteView):
    model=Player
    success_url='/footballers/'
