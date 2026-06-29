"""
Shared axis subplot lesson

Definition: Share x or y axis between subplots.
Why: Easier comparison when axes align.
File: 02_share_axis.py
"""

import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 1, sharex=True)

axs[0].plot([1,2,3,4], [10,20,25,30])
axs[0].set_title('Top')

axs[1].plot([1,2,3,4], [5,15,20,25])
axs[1].set_title('Bottom')

plt.show()

# Practice: Share y-axis instead and observe changes.
