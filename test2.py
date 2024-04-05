import numpy as np
def regionQuery(X, P, eps):
    """
    Bir nuqta atrofidagi qo'shni nuqtalarni topish
    """
    neighbors = []
    for Pn in range(0, len(X)):
        if np.linalg.norm(X[P] - X[Pn]) < eps:
            neighbors.append(Pn)
    return neighbors
def growCluster(X, labels, P, neighborPts, C, eps, minPts):
    """
    Yangi klaster uchun yadro nuqtalarni kengaytirish
    """
    labels[P] = C
    i = 0
    while i < len(neighborPts):
        Pn = neighborPts[i]
        if labels[Pn] == -1:
            labels[Pn] = C
        elif labels[Pn] == 0:
            labels[Pn] = C
            PnNeighborPts = regionQuery(X, Pn, eps)
            if len(PnNeighborPts) >= minPts:
                neighborPts = neighborPts + PnNeighborPts
        i += 1

def dbscan(X, eps, minPts):
    """
    DBSCAN klasterlash algoritmi

    Parametrlar:
    X - ma'lumotlar to'plami (nuqtalar ro'yxati)
    eps - qo'shni nuqtalar orasidagi maksimal masofa
    minPts - yadro nuqta deb hisoblash uchun minimal qo'shni nuqta soni
    """
    labels = [0] * len(X)  # Barcha nuqtalar uchun yorliqlarni 0 (klasterlanmagan) deb belgilash
    C = 0

    for P in range(0, len(X)):
        if not (labels[P] == 0):
            continue
        # P nuqtaning qo'shni nuqtalarini topish
        neighborPts = regionQuery(X, P, eps)
        if len(neighborPts) < minPts:
            labels[P] = -1  # P nuqtani shovqin deb belgilash
        else:
            C += 1
            growCluster(X, labels, P, neighborPts, C, eps, minPts)

    return labels

# Misol ma'lumotlar to'plami va parametrlar
X = np.loadtxt("klasterla.txt", dtype=float)

eps = 1
minPts = 3

# DBSCAN algoritmini ishga tushirish
labels = dbscan(X, eps, minPts)
print(labels)