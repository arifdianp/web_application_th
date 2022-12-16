from django import forms
from .models import Post

class create_form(forms.ModelForm):
    class Meta:
        model = Post
        #fields = ('name','description','mitigation_strategy')
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'mitigation_strategy': forms.Textarea(attrs={'class':'form-control'}),
            'last_updated_by': forms.Select(attrs={'class':'form-control'})
        }
