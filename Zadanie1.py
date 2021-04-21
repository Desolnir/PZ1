import numpy as np
import matplotlib.pylab as plt
import csv
import os.path

x = np.arange(-10,10,0.2)
a = 9.66459

def f(x):
    u = np.sqrt(x*x+a*a)/np.pi
    e = np.exp(abs(1-u))
    y = (-abs(np.sin(x) * np.cos(a) * e))
    return y   

plt.grid()
plt.plot(x, f(x))
plt.show()

if not os.path.exists('results'):
    os.mkdir('results')
res_name = os.path.join(os.getcwd(),'results','massiv8.csv')

with open(res_name, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter="\n")
    for i in range(len(x)):
        Str = [i, x[i], f(x[i])]
        writer.writerow(Str)