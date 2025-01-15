cou = {}


arr = [11,11,11,5,5,18,18]



for i in arr:
   if i in cou:
    cou[i] += 1
   else:
    cou[i] = 1


print(cou)