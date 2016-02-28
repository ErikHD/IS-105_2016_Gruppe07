import matplotlib.pyplot as plt
import numpy as np

#Skift ut verdier etter plot med faktiske verdier

plt.plot([1, 2, 3, 4], [1, 4, 9, 16])

plt.xlabel('time spent')
plt.ylabel('List Size')
plt.title('Time spent searching')
plt.grid(True)
plt.savefig("test.png")
plt.show()