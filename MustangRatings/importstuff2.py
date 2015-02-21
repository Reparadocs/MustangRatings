from ratings.models import Major, Professor, CPairing, MClass
import json

rf = open('realdata/polydump.json','r')

print 'hello'

for i in range(10):
   print 'hi'

num = 0
for line in rf:
   print num
   num += 1
   l = line.strip()
   d = json.loads(l)
   p = Professor(name = d['first_name'] + " " + d['last_name'], polyrating = d['rating'])
   p.save()
   for c in d['classes']:
      cla = MClass.objects.get(name=c)
      cp = CPairing(mclass=cla, professor=p)
      cp.save()

for j in range(5):
   print 'wat'

rf.close()