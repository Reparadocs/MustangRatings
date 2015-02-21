from django.shortcuts import render
from ratings.models import Professor, Major, Rating, CPairing, MClass

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
   return render(request, 'main.html', {'major_list': majors,'form':form)

def professor_list(request, class_id)
   c = MClass.objects.get(id=class_id)
   cpairings = c.cpairing_set.all()
   return render(request, 'list.html', {'pairing_list':cpairings, 'mclass':c})

def pairing_detail(request, cpairing_id):
   pairing = CPairing.objects.get(id=cpairing_id)
   gen_ave = pairing.getAverage():
   your_ave = None
   if request.user.is_authenticated():
      your_ave = pairing.getYourAverage(request.user.userwrapper)
   return render(request, 'detail.html', {'pairing':pairing, 'ave':gen_ave, 'your':your_ave})

   
