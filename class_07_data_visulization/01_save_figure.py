"""
Save figure lesson

Definition: Save plots to image files using `savefig()`.
Why: To include charts in reports or slides.
File: 01_save_figure.py
"""

import matplotlib.pyplot as plt

plt.plot([1,2,3,4], [10,20,25,30])
plt.title('Save Figure Example')

# Save to PNG file
plt.savefig('example_plot.png')

plt.show()

# Expected Output: File `example_plot.png` created in current folder.

# Practice: Save as PDF by changing filename extension to `.pdf`.
