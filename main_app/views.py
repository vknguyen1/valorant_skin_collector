
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Skin, Riot_Account
from .forms import VariantForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

"""
Mock Database for Valorant Skins
"""

# skins = [
#     Skin('vandal', 'reaver', 1775),
#     Skin('sheriff', 'reaver', 1775),
#     Skin('phantom', 'ion', 1775),
#     Skin('operator', 'magepunk', 2600)
# ]


@login_required
def skins_index(request):
    skins = Skin.objects.all()
    return render(request, 'skins/index.html', {'skins': skins})

@login_required
def skins_detail(request, skin_id):
    skin = Skin.objects.get(id=skin_id)
    variant_form = VariantForm()
    return render(request, 'skins/detail.html', {
        'skin': skin,
        'variant_form': variant_form,
        })
 
@login_required
def add_variant(request, skin_id):
    form = VariantForm(request.POST)

    if form.is_valid():
        new_variant = form.save(commit=False)
        new_variant.skin_id = skin_id
        new_variant.save()
    return redirect('detail', skin_id=skin_id)


@login_required
def assoc_account(request, skin_id, riot_account_id):
    Skin.objects.get(id=skin_id).riot_accounts.add(riot_account_id) 
    return redirect('detail', cat_id=cat_id)

def signup(request):
    # define tasks for handling POST request
    form = UserCreationForm()
    error_message = ''
    
    if request.method == 'POST':
        # capture form inputs from the usercreation form
        form = UserCreationForm(request.POST)
        # validate the form inputs
        if form.is_valid():
            # save the input values as a new user to the DB
            user = form.save()
            # programmatically log the user in
            login(request, user)
            # redirect the user to the cats index page
            return redirect('index')
        # if form is invalid, show error message
        else:
            error_message = 'invalid credentials'
    # define tasks for handling GET request
    context = {'form': form, 'error_message': error_message}
    # render a template with an empty formzz6bnn
    return render(request, 'registration/signup.html', context)

class SkinCreate(CreateView):
    model = Skin
    fields = '__all__'
    

class SkinUpdate(UpdateView):
    model = Skin
    fields = '__all__'

class SkinDelete(DeleteView):
    model = Skin
    success_url = '/skins/'

class Account_Index(LoginRequiredMixin, ListView):
    model = Riot_Account

class Account_Create(LoginRequiredMixin,CreateView):
    model = Riot_Account
    fields = '__all__'

class Account_Detail(LoginRequiredMixin,DetailView):
    model = Riot_Account

class Account_Delete(LoginRequiredMixin,DeleteView):
    model = Riot_Account
    success_url = '/Accounts/'

class Account_Update(LoginRequiredMixin,UpdateView):
    model = Riot_Account
    fields = '__all__'
