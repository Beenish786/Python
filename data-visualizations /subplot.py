import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pollution=[32,54,45,67,98,42,82, 74]
City=['Sahiwal', 'pindi', 'lahore', 'harapa','town','city','isalbamd','muree']

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1) 
plt.bar(City, pollution, color='skyblue')
plt.subplot(1, 2, 1)
plt.show()
