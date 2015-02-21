from django.db import models
from django.contrib.auth.models import User

class Major(models.Model):
   name = models.CharField(max_length=30)

class MClass(models.Model):
   major = models.ForeignKey(Major)
   number = models.IntegerField()

class Professor(models.Model):
   name = models.CharField(max_length=100)
   polyrating = models.CharField(max_length=10)

class CPairing(models.Model):
   professor = models.ForeignKey(Professor)
   mclass = models.ForeignKey(MClass)

   def getAverage():
      total = 0.0
      for rating in self.rating_set:
         total += rating.rating

class UserWrapper(models.Model):
   owner = models.OneToOneField(User)

   def getMajorAverage(self, major):
      total = 0.0
      stotal = 0.0
      num = 0
      for rating in self.rating_set:
         if rating.major is major:
            num += 1
            total += rating.rating
            stotal += rating.cpairing.average
      ave1 = total/num
      ave2 = stotal/num
      return ave1-ave2
   
   def getGeneralAverage(self):
      total = 0.0
      stotal = 0.0
      num = len(self.rating_set.all())
      for rating in self.rating_set:
         total += rating.rating
         stotal += rating.cpairing.average
      ave1 = total/num
      ave2 = stotal/num
      return ave1-ave2

class Rating(models.Model):
   owner = models.ForeignKey(UserWrapper)
   rating = models.FloatField()
   cpairing = models.ForeignKey(CPairing)
   major = models.ForeignKey(Major)

