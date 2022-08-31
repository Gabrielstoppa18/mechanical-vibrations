from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import scipy.interpolate as interpolate


def openFile():

    filepath ='Coleta2_0_5.txt'
    file = open(filepath, 'r')
    arq = file.read().splitlines()
    print("Arquivo lido")
    return arq

data=openFile()
x_acc=[]
for i in range(195,301):
    x_acc.append(float(data[i]))

#print(x_acc)

x_acc=np.array(x_acc)
y = np.arange(x_acc.size)
# Interpolate the data using a cubic spline to "new_length" samples
new_length = 300-195
new_y = np.linspace(y.min(), y.max(), new_length)
new_x = interpolate.interp1d(x_acc,y, kind='quadratic')(new_y)

#plt.plot(x,y_acc,'r')
plt.plot(new_y,new_x,'b')
#plt.xlim([195,300])
plt.show()


