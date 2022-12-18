from django import forms
from .models import Post

PROGRESS_CHOICES = ("Not Mitigated", "Partially Mitigated", "Fully Mitigated")


class create_form(forms.ModelForm):
    class Meta:
        model = Post
        #fields = ('name','description','mitigation_strategy')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control col-sm-5'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'mitigation_strategy': forms.Textarea(attrs={'class':'form-control'}),
            'mitigation_progress': forms.Select(attrs={'class':'form-control col-sm-2'}),
            'last_updated_by': forms.TextInput(attrs={'class':'form-control','value':'a','id':'who_updates', 'type':'hidden'})
        }

class edit_form(forms.ModelForm):
    class Meta:
        model = Post
        #fields = ('name','description','mitigation_strategy')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'mitigation_strategy': forms.Textarea(attrs={'class':'form-control'}),
            #'mitigation_progress': forms.ChoiceField(choices=PROGRESS_CHOICES),
            'last_updated_by': forms.TextInput(attrs={'class':'form-control','value':'a','id':'who_updates', 'type':'hidden'})
        }
