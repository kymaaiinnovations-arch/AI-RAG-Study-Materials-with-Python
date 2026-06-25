"""
Legend lesson

Definition: Legends explain plotted series when multiple datasets are present.
Why: To identify which line or marker corresponds to which dataset.
File: 02_legend.py
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y1 = [10,20,25,30]
y2 = [5,15,20,25]

plt.plot(x, y1, label='Dataset A')
plt.plot(x, y2, label='Dataset B')
plt.legend()
plt.title('Legend Example')

plt.show()

# Practice: Move legend to the upper left using `loc` argument.
