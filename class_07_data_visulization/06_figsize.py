"""
Figure size lesson

Definition: Change figure size to control chart dimensions.
Why: To make charts larger or smaller for presentations.
File: 06_figsize.py
"""

import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot([1,2,3,4], [10,20,25,30])
plt.title('Figure Size Example')

plt.show()

# Practice: Try a square figure with `figsize=(6,6)`.
