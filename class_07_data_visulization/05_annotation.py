"""
Annotation lesson

Definition: Add text annotations to highlight points.
Why: To call attention to specific values.
File: 05_annotation.py
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x, y, marker='o')
plt.annotate('Peak', xy=(4,30), xytext=(3,28), arrowprops=dict(arrowstyle='->'))
plt.title('Annotation Example')

plt.show()

# Practice: Annotate the first data point as 'Start'.
