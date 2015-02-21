from django.shortcuts import render
from ratings.modles import Major, Class, 

# Create your views here.
def main(request):
   if request.user.is_authenticated():
      if request.method == 'GET':
	     majorList = Major.objects.all()
		 mForm = MajorForm();
		 return render(request, {'form' : mForm, 'majorList' : majorList})
	  elif request.method == 'POST':
	     
		 return redirect('list', args=(request,classID))

	else #needs to log on	 
		 
		 
def list(request, classID):
   classList = Class.objects.all()
   c = MClass.objects.get(id=classID)
   professors = c.getProfessors()
   return render(request, {'professors', professors})
	
	
   #find class from classID