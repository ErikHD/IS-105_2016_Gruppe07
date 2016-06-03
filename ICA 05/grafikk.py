import matplotlib.pyplot as plt
import numpy as np

#legger inn verdier her, x for tidsbruk y for listestoerrelse

plt.plot([0, 2.78, 13.97, 48.65], [0, 100, 500, 1000])

#Gir navn til x og y akser og figuren, samt tegner selve figuren

plt.xlabel('time spent')
plt.ylabel('List Size')
plt.title('Time spent searching')
plt.grid(True)
plt.savefig("test.png")
plt.show()