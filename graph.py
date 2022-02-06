from tkinter import N
import matplotlib.pyplot as plt
import numpy as np

X, Y = np.loadtxt('bank.txt', delimiter=',', unpack=True)
 
plt.plot(X, Y)
plt.title('Hypixel Skyblock Money in Bank')
plt.xlabel('X')
plt.ylabel('Y')
current_values = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:.0f}'.format(x) for x in current_values])
plt.show()