import matplotlib.pyplot as plt
import numpy as np
x_soat=np.array([1.0, 2.0, 3.0])
y_baho=np.array([2.0, 4.0, 6.0])
#To'g'ri hisoblash uchun funksiya
def forward(x):
    return x*w
#Xatolik loosning funksiyasi
def Loss(x,y):
    y_pred=forward(x)
    return (y_pred - y)**2
#Grafikni yaratib olishimiz uchun konteynerlar
w_list=[]
mse_list=[]
#w ni 0 dan 4 gacha oraliqda hisoblash
for w in np.arange(0.0,4.1,0.1):
    print("w={:.3f}".format(w))
    l_umum=0
    for x_hb_qiym, y_hb_qiym in zip(x_soat,y_baho):
        y_hb_bash = forward(x_hb_qiym)
        L_hb_qiym = Loss(x_hb_qiym, y_hb_qiym)
        l_umum+=L_hb_qiym
        print("\t", "{:.2f},{:.2f},{:.2f},{:.2f}".format(x_hb_qiym,y_hb_qiym,y_hb_bash,L_hb_qiym))
    # Har bir malumot chun MSEni hisoblaymiz
    print("MSE=",l_umum/len(x_soat)) #len(x_soat ==> N)
    w_list.append(w)
    mse_list.append(l_umum/len(x_soat))
#Grafik natija
plt.plot(w_list,mse_list)
plt.ylabel('Loss')
plt.xlabel('w')
ax= plt.axes()
ax.set_facecolor('#030101')
plt.show()



#oddiy regressiya
"""x=np.loadtxt("Oddiy_regressiya_lesson.txt", dtype=float)
b=np.transpose(x)
print(np.mean(b[1]))
sum1=0
sum2=0
for j in range(len(x[0])):
    sum1+=(b[1][j]-np.mean(b[1]))*(b[2][j]-np.mean(b[2]))
    sum2+=(b[1][j]-np.mean(b[1]))**2
m= sum1/sum2
c=np.mean(b[2]) - np.mean(b[1])*m
print(f"y = {m}*x + {c}")"""