from django.db import models
from django.contrib.auth.models import User

class Major(models.Model):
   name = models.CharField(max_length=30)

   def __unicode__(self):
      return self.name

   def getClasses(self):
      return self.mclass_set

class MClass(models.Model):
   major = models.ForeignKey(Major)
   number = models.CharField(max_length=10)
   name = models.CharField(max_length=50)

   def getProfessors(self):
      profs = []
      for cpair in self.cpairing_set.all():
         profs.append(cpair.professor)
      return profs

class Professor(models.Model):
   name = models.CharField(max_length=100)
   polyrating = models.CharField(max_length=10)

   def getPairings(self):
      return self.cpair_set

class CPairing(models.Model):
   professor = models.ForeignKey(Professor)
   mclass = models.ForeignKey(MClass)

   def getYourAverage(self, user):
      ave = self.getAverage()
      majorAve = user.getMajorAverage(self.mclass.major)
      genAve = user.getGeneralAverage()
      userAve = (majorAve*2 + genAve)/3
      return ave+userAve

   def getAverage(self):
      total = 0.0
      for rating in self.rating_set.all():
         total += rating.rating
      if total == 0:
         return 0
      return total/len(self.rating_set.all())

class UserWrapper(models.Model):
   owner = models.OneToOneField(User)

   def getMajorAverage(self, major):
      total = 0.0
      stotal = 0.0
      num = 0
      for rating in self.rating_set.all():
         if rating.major == major:
            num += 1
            total += rating.rating
            stotal += rating.cpairing.getAverage()
      if num == 0:
         return 0
      ave1 = total/float(num)
      ave2 = stotal/float(num)
      return ave1-ave2
   
   def getGeneralAverage(self):
      total = 0.0
      stotal = 0.0
      num = len(self.rating_set.all())
      for rating in self.rating_set.all():
         total += rating.rating
         stotal += rating.cpairing.getAverage()
      if num == 0:
         return 0
      ave1 = total/float(num)
      ave2 = stotal/float(num)
      return ave1-ave2

class Rating(models.Model):
   owner = models.ForeignKey(UserWrapper)
   rating = models.FloatField()
   cpairing = models.ForeignKey(CPairing)
   major = models.ForeignKey(Major)

