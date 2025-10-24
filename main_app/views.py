from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Army, Battle
from .forms import BattleForm
from django.urls import reverse

# Import HttpResponse to send text-based responses
from django.http import HttpResponse

# Define the home view function
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

class ArmyCreate(LoginRequiredMixin, CreateView):
    model = Army
    fields = ['name', 'nationality', 'size', 'weapons', 'year', 'leader', 'details']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def army_index(request):
    armies = Army.objects.filter(user=request.user)
    # Render the armies/index.html template with the armies data
    return render(request, 'armies/index.html', {'armies': armies})

@login_required
def army_detail(request, army_id):
    try:
        army = Army.objects.get(id=army_id, user=request.user)
    except Army.DoesNotExist:
        return redirect('army_index')

    battles = Battle.objects.filter(army=army)
    battle_form = BattleForm()
    return render(request, 'armies/detail.html', {
        'army': army,
        'battle_form': battle_form,
        'battles': battles
    })
 
class ArmyUpdate(LoginRequiredMixin, UpdateView):
    model = Army
    fields = ['size', 'weapons', 'details']

class ArmyDelete(LoginRequiredMixin, DeleteView):
    model = Army
    success_url = '/armies/'

@login_required
def add_battle(request, army_id):
    form = BattleForm(request.POST)
    if form.is_valid():
        new_battle = form.save(commit=False)
        new_battle.army_id = army_id
        new_battle.save()
    return redirect('army-detail', army_id=army_id)

class BattleUpdate(LoginRequiredMixin, UpdateView):
    model = Battle
    form_class = BattleForm
    template_name = 'battles/update.html'
    pk_url_kwarg = 'battle_id'

    def get_success_url(self):
        return reverse('army-detail', kwargs={'army_id': self.object.army_id})

    def get_queryset(self):
        return Battle.objects.filter(army__user=self.request.user)

    def form_valid(self, form):
        return super().form_valid(form)

class BattleDelete(LoginRequiredMixin, DeleteView):
    model = Battle
    template_name = 'battles/delete.html'
    pk_url_kwarg = 'battle_id'

    def get_success_url(self):
        return reverse('army-detail', kwargs={'army_id': self.object.army_id})

    def get_queryset(self):
        return Battle.objects.filter(army__user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['army_id'] = self.object.army_id
        return context

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('army-index')
        else:
            error_message = 'Invalid sign-up: please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
