import numpy as np
x=np.loadtxt("klassifikatsiya_ozgaruvchi_tanlanmasi.txt", dtype=float)
k=int(input('k = '))
if k%2==0:
    print("k juft son bo'lishi mumkin emas")
    breakpoint()
birinchisinf=0
ikkinchisinf=0
a=[]
for i in range(len(x[0])-1):
    a.append(float(input(f"a{i} = ")))
    i+=1
masofa=[float()]
for i in range(len(x)):
    masofa.append((((x[i][0]-a[0])**2)+((x[i][1]-a[1])**2)+((x[i][2]-a[2])**2))**(1/2))
masofa2 = sorted(masofa)
for i in range(k):
    for j in range(len(x)):
       if masofa2[i] == masofa[j]:
           if x[j][len(x[0])-1] == 0:
               birinchisinf+=1
           elif x[j][len(x[0])-1]==1:
               ikkinchisinf +=1
       j+=1
    i+=1
if birinchisinf>ikkinchisinf:
    print("birinchi sinfga tegishli")
else:
    print("ikkinchi sinfga tegishli")