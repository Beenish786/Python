import matplotlib.pyplot as plt

data = [10, 15, 12, 18, 20, 10, 12, 15, 18, 15]

plt.boxplot(data)
plt.title('Box and Whisker Plot')
plt.ylabel('Value')
plt.show()
