from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User, Group

new_group, created = Group.objects.get_or_create(name ='Risk Consultant')
new_group2, created = Group.objects.get_or_create(name ='Project Manager')


class create_form(forms.ModelForm):
    class Meta:
        model = Post
        #fields = ('name','description','mitigation_strategy')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control col-sm-5'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'mitigation_strategy': forms.Textarea(attrs={'class':'form-control', 'id':'Strategy'}),
            'mitigation_progress': forms.Select(attrs={'class':'form-control col-sm-2', 'id':'mp'}),
            'last_updated_by': forms.TextInput(attrs={'class':'form-control','value':'a','id':'who_updates', 'type':'hidden'})
        }

class edit_form(forms.ModelForm):
    class Meta:
        model = Post
        #fields = ('name','description','mitigation_strategy')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'mitigation_strategy': forms.Textarea(attrs={'class':'form-control', 'id':'Strategy'}),
            'mitigation_progress': forms.Select(attrs={'class':'form-control col-sm-2','id':'mp'}),
            'last_updated_by': forms.TextInput(attrs={'class':'form-control','value':'a','id':'who_updates', 'type':'hidden'})
        }

class signup_form(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(signup_form, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class addstatus_form(UserChangeForm):

    class Meta:
        model = User
        fields = ('groups', )

    def __init__(self, *args, **kwargs):
        super(addstatus_form, self).__init__(*args, **kwargs)
        #self.fields['username'].widget.attrs['class'] = 'form-control'
