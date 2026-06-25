"""
Tight layout lesson

Definition: Use `tight_layout()` to prevent overlapping labels.
Why: Ensures readability when subplots are close.
File: 03_tight_layout.py
"""

import matplotlib.pyplot as plt

fig, axs = plt.subplots(2,2)

for i, ax in enumerate(axs.flat, start=1):
    ax.plot([1,2,3], [i, i*2, i*3])
    ax.set_title(f'Subplot {i}')

plt.tight_layout()
plt.show()

# Practice: Remove `tight_layout()` and see the difference.
