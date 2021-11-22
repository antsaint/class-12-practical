import matplotlib.pyplot as plt
import numpy as np


quantity = np.array([35, 25, 69, 70])
my_labels = ['Apple', 'Pineapple', 'banana', 'lolcat']

plt.pie(quantity, labels = my_labels)
plt.show()