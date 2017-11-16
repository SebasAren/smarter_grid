import data_structure
import data_generator

import matplotlib.pyplot as plt

x = [1, 2]
y = [5, 10]

x1 = [2, 4]
y1 = [3, 3]


plt.scatter(x, y, color= 'k', marker = '^', s = 50)

plt.scatter(x1, y1, color= 'k', marker = 'x', s = 50)

plt.grid(b = True, axis = 'both')

plt.axis((0,5,0,10))

plt.xlabel('x')
plt.xlabel('y')
plt.title('test_wijk')
plt.legend()
plt.show()


