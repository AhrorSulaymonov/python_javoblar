import random
import numpy as np
x = np.loadtxt("klasterizatsiya.txt", dtype=float)
a = np.random.rand(2, len(x[0]))
i = random.randint(0, len(x)-1)
a[0] = x[i]
j = random.randint(0, len(x)-1)
if i == j:
    j = random.randint(0, len(x)-1)
a[1] = x[j]
masofa = []
mas = 0
for i in range(2):
    for k in range(len(x)):
        for j in range(len(x[0])):
            mas += (a[i][j]-x[k][j])**2
        masofa.append(mas**(1/2))
        mas = 0
minms = []
for j in range(len(x)):
    minm = masofa[j]
    for i in range(2):
        minm = np.minimum(minm, masofa[j+i*len(x)])
    minms.append(minm)
klasterlanganmatritsa = np.random.rand(len(x), len(x[0])+1)
for i in range(len(x)):
    for j in range(len(x[0])):
        klasterlanganmatritsa[i][j] = x[i][j]
sinf1son = 0
sinf2son = 0
sinfraqami = 0
for i in range(len(minms)):
    for j in range(len(masofa)):
        if minms[i] == masofa[j]:
            sinfobyekti = j % len(x)
            sinfraqami = j//len(x)
    klasterlanganmatritsa[i][len(x[0])] = sinfraqami
for i in range(len(klasterlanganmatritsa)):
    if klasterlanganmatritsa[i][len(x[0])] == 0:
        sinf1son += 1
    elif klasterlanganmatritsa[i][len(x[0])] == 1:
        sinf2son += 1
sinfbir = np.random.rand(sinf1son, len(klasterlanganmatritsa[0]))
sinfikki = np.random.rand(sinf2son, len(klasterlanganmatritsa[0]))
j = 0
k = 0
for i in range(len(klasterlanganmatritsa)):
    if klasterlanganmatritsa[i][len(x[0])] == 0:
        sinfbir[j] = klasterlanganmatritsa[i]
        j += 1
    elif klasterlanganmatritsa[i][len(x[0])] == 1:
        sinfikki[k] = klasterlanganmatritsa[i]
        k += 1
ng = 0
for ng in range(50):
    sinfbirT = np.transpose(sinfbir)
    sinfikkiT = np.transpose(sinfikki)
    for i in range(2):
        for j in range(len(x[0])):
            if i == 0:
                a[i][j] = np.mean(sinfbirT[j])
            elif i == 1:
                a[i][j] = np.mean(sinfikkiT[j])
    masofa = []
    mas = 0
    for i in range(2):
        for k in range(len(x)):
            for j in range(len(x[0])):
                mas += (a[i][j] - x[k][j]) ** 2
            masofa.append(mas ** (1 / 2))
            mas = 0
    minms = []
    for j in range(len(x)):
        minm = masofa[j]
        for i in range(2):
            minm = np.minimum(minm, masofa[j + i * len(x)])
        minms.append(minm)
    klasterlanganmatritsa = np.random.rand(len(x), len(x[0]) + 1)
    for i in range(len(x)):
        for j in range(len(x[0])):
            klasterlanganmatritsa[i][j] = x[i][j]
    sinf1son = 0
    sinf2son = 0
    sinfraqami = 0
    for i in range(len(minms)):
        for j in range(len(masofa)):
            if minms[i] == masofa[j]:
                sinfobyekti = j % len(x)
                sinfraqami = j // len(x)
        klasterlanganmatritsa[i][len(x[0])] = sinfraqami
    for i in range(len(klasterlanganmatritsa)):
        if klasterlanganmatritsa[i][len(x[0])] == 0:
            sinf1son += 1
        elif klasterlanganmatritsa[i][len(x[0])] == 1:
            sinf2son += 1
    sinfbir = np.random.rand(sinf1son, len(klasterlanganmatritsa[0]))
    sinfikki = np.random.rand(sinf2son, len(klasterlanganmatritsa[0]))
    j = 0
    k = 0
    for i in range(len(klasterlanganmatritsa)):
        if klasterlanganmatritsa[i][len(x[0])] == 0:
            sinfbir[j] = klasterlanganmatritsa[i]
            j += 1
        elif klasterlanganmatritsa[i][len(x[0])] == 1:
            sinfikki[k] = klasterlanganmatritsa[i]
            k += 1
print(klasterlanganmatritsa)
