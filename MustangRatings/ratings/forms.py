from django import forms
from ratings.models import Major

class ClassForm(forms.Form):
   major = forms.ModelChoiceField(label='Major', queryset=Major.objects.all())
   number = forms.CharField(label='Class Number', max_length=10) 

class RatingForm(forms.Form):
   rating = forms.FloatField(min_value = 0, max_value= 10)

   
