KLocation = ('28.538330', '-81.378883')
KLat = float(KLocation[0])
KLong = float(KLocation[1])

ALocation = ('40.963987', '-75.960642')
ALat = float(ALocation[0])
ALong = float(ALocation[1])

VLocation = ('27.947420', '-82.458778')
VLat = float(VLocation[0])
VLong = float(VLocation[1])

#Print the locations of all my friends
print("My location is", KLat, ", ", KLong, ".\n")
print("Aseel's location is", ALat, ",", ALong, ".\n")
print("Valeria's location is", VLat, ", ", VLong, ".\n")

#Find the difference
KandA = ((KLat - ALat) / (KLong - ALong))
KandV = ((KLat - VLat) / (KLong - VLong))

#Which friend is the furthest away?
if(KandA > KandV):
  print("Aseel is the furthest away from me.")
elif(KandA < KandV):
  print("Valeria is the furthest away from me.")
else:
  print("There are both the same distance away from me.")
