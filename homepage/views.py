from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import create_form
#def home(request):
#    return render(request, 'home.html', {'name':'mosh'})

class home(ListView):
    model = Post
    template_name = 'home.html'

class create_risk(CreateView):
    model = Post
    form_class = create_form
    template_name = 'create_risk.html'
