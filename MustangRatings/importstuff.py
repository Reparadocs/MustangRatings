from ratings.models import Major, Professor, CPairing, MClass
import json

majorfile = open('realdata/majorlist.txt','r')
classfile = open('realdata/classes.json','r')

for line in majorfile:
   n = line.strip()
   m = Major(name=n)
   m.save()

for line in classfile:
   l = line.strip()
   d = json.loads(l)
   for maj in d:
      m = Major.objects.get(name=maj)
      for num in d[maj]:
         c = MClass(major=m, number=num, name=maj + " " + num)
         c.save()

majorfile.close()
classfile.close()
