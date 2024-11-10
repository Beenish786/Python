import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt

pollution=[32,54,45,67,98,42,82, 74]
City=['Sahiwal', 'pindi', 'lahore', 'harapa','town','city','isalbamd','muree']

plt.figure(figsize=(10, 6))
plt.plot(City, pollution, color='skyblue')
plt.show()
