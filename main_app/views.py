from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Player, Trophy
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
    id_list = footballer.titles.all().values_list('id')
    honors_not_won = Trophy.objects.exclude(id__in=id_list)
    wage_form = WageForm()
    return render(request, 'football/detail.html', {'player': footballer, 'wage_form': wage_form, 'trophies': honors_not_won})

def add_wage(request, player_id):
    wage_form = WageForm(request.POST)
    if wage_form.is_valid():
        new_paystub = wage_form.save(commit=False)
        new_paystub.player_id = player_id
        new_paystub.save()
    return redirect('player', player_id=player_id)

def add_title(request, player_id, trophy_id):
    Player.objects.get(id=player_id).titles.add(trophy_id)
    return redirect('player', player_id=player_id)

class EnterPlayer(CreateView):
    model=Player
    fields=['name','age','position','mkt_value','contract_exp']

class UpdatePlayer(UpdateView):
    model=Player
    fields=['age','position','mkt_value', 'contract_exp']

class DeletePlayer(DeleteView):
    model=Player
    success_url='/footballers/'

class TrophyList(ListView):
    model = Trophy

class TrophyCreate(CreateView):
    model=Trophy
    fields='__all__'
    print(object)

class TrophyDetail(DetailView):
    model=Trophy

class TrophyUpdate(UpdateView):
    model=Trophy
    fields=['title']

class TrophyDelete(DeleteView):
    model=Trophy
    print(object)
    success_url='/trophies/'