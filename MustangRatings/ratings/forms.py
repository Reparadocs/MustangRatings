from django import forms
from ratings.models import Major

class ClassForm(forms.Form):
   major = forms.ModelChoiceField(label='Major', queryset=Major.objects.all())
   number = forms.CharField(label='Class Number', max_length=10) 
   
