import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pollution=[32,54,45,67,98,42,82, 74]
City=['Sahiwal', 'pindi', 'lahore', 'harapa','town','city','okara','muree']

plt.hist(pollution, bins=10)
plt.show()
