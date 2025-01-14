matrics = [
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]
]                 


for i in range(len(matrics)):
      matrics[i][i] = 1

for row in matrics:
   print(" ".join(map(str,row)))