import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pollution=[32,54,45,67,98,42,82, 74]
City=['Sahiwal', 'pindi', 'lahore', 'harapa','town','city','okara','muree']

plt.figure(figsize=(8, 8))  # Optional: Set figure size
plt.pie(pollution, labels=City, autopct='%1.1f%%', colors=plt.cm.Paired.colors, startangle=90)
plt.show()
