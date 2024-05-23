import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# funcao
def func(t, d, a, b, w, phi):
    return (d+a*np.exp(-b*t)*np.cos(w*t+phi))

# dados
x_data = np.loadtxt('./output/tempos.txt', dtype=float)
y_data = np.loadtxt('./output/espacos.txt', dtype=float)

# plotando dados experimentais
plt.plot(x_data, y_data, 'bo')


# palpite de parametros
guess = [0.12, 0.1, 0, 2*np.pi, 0]

# perform curve fit
popt, pcov = curve_fit(func, x_data, y_data, guess)

b = popt[2]
w0 = np.sqrt(popt[3]**2 + b**2)
m = 0.102
q = m * w0 / (2 * m * b) # fator de qualidade

f = open('./output/fqualidade.txt', 'w')
f.write(f'{q}')
f.close

print(popt)

x_fit = np.arange(0.0, 61, 0.01)

plt.plot(x_fit, func(x_fit, *popt), 'r')

plt.axis((0, 65, 0, 0.25))
plt.show()
