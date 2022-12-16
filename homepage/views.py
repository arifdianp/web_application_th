from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import create_form, edit_form
from django.urls import reverse_lazy

#def home(request):
#    return render(request, 'home.html', {'name':'arif'})

class home(ListView):
    model = Post
    template_name = 'home.html'

class create_risk(CreateView):
    model = Post
    form_class = create_form
    template_name = 'create_risk.html'

class edit_risk(UpdateView):
    model = Post
    form_class = edit_form
    template_name = 'edit_risk.html'

class delete_risk(DeleteView):
    model = Post
    template_name = 'delete_risk.html'
    success_url = reverse_lazy('home')

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        answer = Post.objects.filter(name__contains=searched)
        return render(request, 'search.html', {'searched':searched, 'answer':answer})
    else:
        return render(request, 'search.html',{})
