from django.shortcuts import render
from ratings.models import Professor, Major, Rating, CPairing, MClass

def main(request):
   majors = Major.objects.all()
   return render(request, 'main.html', {'major_list': majors})

def professor_list(request):
   professors = Professor.objects.all()
   nprof = []
   for i in range(10):
      nprof.append(professors[i])
   return render(request, 'list.html', {'professor_list':nprof})

def professor_detail(request):
   professor = CPairing.objects.all()[0]
   return render(request,'detail.html', {'cpairing':professor})

