from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import create_form, edit_form, signup_form, addstatus_form
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

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
        answer = Post.objects.filter(Q(name__contains=searched) | Q(description__contains=searched) | Q(mitigation_strategy__contains=searched))
        return render(request, 'search.html', {'searched':searched, 'answer':answer})
    else:
        return render(request, 'search.html',{})


## authentication part
#class userRegister(CreateView):
#    form_class = signup_form
#    template_name = 'register.html'
#    success_url = reverse_lazy('login')

class userStatus(UpdateView):
    form_class = addstatus_form
    template_name = 'addstatus.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user

def userRegister(request):
    if request.method == "POST":
        form = signup_form(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)

            login(request, user)
            messages.success(request, ("Registration successful"))
            return redirect('addstatus')
    else:
        form = signup_form()
    return render(request, 'register.html',{'form':form})
