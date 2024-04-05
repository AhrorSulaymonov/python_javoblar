import numpy as np
"""A=[[2,3],[2,4],[6,7]]
print(np.shape(A))
a=np.random.randint(1,20,8).reshape(-1,4)
print(a)
c=np.mean(a[1])
print(c)
a=np.transpose(a)
print(a)"""
# birinchi shart bo'yicha normallashtirish
x=np.loadtxt("iris.txt", dtype=float)
b=np.transpose(x)
for i in range(len(b)-1):
    for j in range(len(b[0])):
        b[i][j]=((b[i][j]-np.min(b[i]))/(np.max(b[i])-np.min(b[i])))
x=np.transpose(b)
print(x)
# ikkinchi shart bo'yicha normallashtirish
"""
x=np.loadtxt("iris.txt", dtype=float)
b=np.transpose(x)
for i in range(len(b)-1):
    for j in range(len(b[0])):
        b[i][j]=((b[i][j]-np.mean(b[i]))/(np.max(b[i])-np.mean(b[i])))
x=np.transpose(b)
print(x)"""
# uchinchi shart bo'yicha normallashtirish (a;b) oraliqda
""""a=int(input())
b=int(input())
long=b-a
x=np.loadtxt("iris.txt", dtype=float)
b=np.transpose(x)
for i in range(len(b)-1):
    for j in range(len(b[0])):
        b[i][j]=((b[i][j]-np.min(b[i]))/(np.max(b[i])-np.min(b[i])))*long+a


x=np.transpose(b)
print(x)"""

import numpy as np

"""x = np.loadtxt("iris.txt", dtype=float)

y = [[0 for i in range(len(x[0]))] for j in range(len(np.transpose(x)[0]))]
a = int(input("a="))
b = int(input("b="))
t = np.transpose(x)

for i in range(len(np.transpose(x)[0])):
    for j in range(len(x[0])):
        if (j != len(x[i]) - 1):
            y[i][j] = a + (x[i][j] - np.min(t[j])) * (b - a) / (np.max(t[j]) - np.min(t[j]))
        else:
            y[i][j] = x[i][j]

for i in y:
    print(i)"""

"""x = np.loadtxt("iris.txt", dtype=float)

y = [[0 for i in range(len(x[0]))] for j in range(len(np.transpose(x)[0]))]

t = np.transpose(x)

for i in range(len(np.transpose(x)[0])):
    for j in range(len(x[0])):
        if (j != len(x[i])-1):
            y[i][j] = (x[i][j] - np.mean(t[j])) / (np.max(t[j]) - np.min(t[j]))
        else:
            y[i][j]=x[i][j]


for i in y:
    print(i)"""
