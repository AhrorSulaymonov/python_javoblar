import pandas as pd
df=pd.read_csv('data.csv', delimiter=', ')
print(df)
alfa=0.001#o'rganish tezligi
w=[1, 2]#Koeffisientlarni dastlabki qiymati
costOld=10**10#Oldingi iteratsiyaning xatolik funksiyasi qiymati
cost=10**10#
epsilon=0.0001
while(True):
    costOld=cost
    w1=[0, 0]
    print('function: f(x)='+ str(w[0])+'+'+str(w[1])+'*x')
    cost=0
    for i in range(df.shape[0]):
        #print(df['y'][i])
        cost+=(w[0]+w[1]*df['x'][i]-df['y'][i])**2
    cost=cost/(2*6)
    print('cost=', cost)


    summa=0
    for i in range(df.shape[0]):
        summa+=(w[0] + w[1] * df['x'][i]-df['y'][i])
    w1[0]=w[0]-alfa*(1/6)*summa
    summa1 = 0
    for i in range(df.shape[0]):
        summa1 += (w[0] + w[1] * df['x'][i] - df['y'][i])*df['x'][i]
    w1[1] = w[1] - alfa * (1 / 6) * summa1
    w[0]=w1[0]
    w[1]=w1[1]
    if(costOld-cost<epsilon):
        break

print(w[0]+w[1]*7)
print(w[0]+w[1]*10)
print(w[0]+w[1]*25)
print(w[0]+w[1]*64)
print(w[0]+w[1]*15)