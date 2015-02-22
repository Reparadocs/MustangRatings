from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from ratings.forms import RatingForm, ClassForm
from ratings.models import Professor, Major, Rating, CPairing, MClass, UserWrapper

def index(request):
   if request.user.is_authenticated():
      return redirect(reverse('main'))
   else:
      return render(request, 'index.html')

def register(request):
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
         new_user = form.save()
         wrapper = UserWrapper(owner=new_user)
         wrapper.save()
         return HttpResponseRedirect("/ratings/")
   else:
      form = UserCreationForm()
   return render(request, "registration/register.html", {'form': form,})

def main(request):
   if request.method == 'POST':
      form = ClassForm(data=request.POST)
      if form.is_valid():
         c = MClass.objects.filter(major=form.cleaned_data['major'])
         c = c.objects.get(number=form.cleaned_data['number'])
         return redirect(reverse('professor_list', args=(c[0].id,)))
   else:
      form = ClassForm()
      majors = Major.objects.all()
   return render(request, 'main.html', {'major_list': majors,'form':form})

def professor_list(request, class_id):
   c = MClass.objects.get(id=class_id)
   cpairings = c.cpairing_set.all()
   return render(request, 'list.html', {'pairing_list':cpairings, 'mclass':c})

def pairing_detail(request, cpairing_id):
   pairing = CPairing.objects.get(id=cpairing_id)
   gen_ave = pairing.getAverage()
   your_ave = None
   form = None
   login_url = "/ratings/login/?next=/ratings/detail/"+str(cpairing_id)
   if request.method == 'POST':
      if request.user.is_authenticated():
         form = RatingForm(data=request.POST)
         if form.is_valid():
            r = Rating(owner=request.user.userwrapper, rating=form.cleaned_data['rating'], cpairing=pairing, major=pairing.mclass.major)
            r.save()
   if request.user.is_authenticated():
      your_ave = pairing.getYourAverage(request.user.userwrapper)
      form = RatingForm()
   return render(request, 'detail.html', {'pairing':pairing, 'ave':gen_ave, 'your':your_ave, 'form':form, "login_url":login_url})

   
