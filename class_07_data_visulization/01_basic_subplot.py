"""
Basic subplot lesson

Definition: Show multiple plots in one figure using subplots.
Why: Compare multiple charts side-by-side.
File: 01_basic_subplot.py
"""

import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(8,3))

axs[0].plot([1,2,3], [2,4,6])
axs[0].set_title('Plot A')

axs[1].plot([1,2,3], [1,3,2])
axs[1].set_title('Plot B')

plt.tight_layout()
plt.show()

# Practice: Create a 2x2 grid of subplots.
