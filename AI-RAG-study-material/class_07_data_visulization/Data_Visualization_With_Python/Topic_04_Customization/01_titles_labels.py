"""
Titles and labels lesson

Definition: Add titles and axis labels to make charts understandable.
Why: Helps the viewer know what the chart represents.
File: 01_titles_labels.py
"""

import matplotlib.pyplot as plt

x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x, y)
plt.title("Demo: Title and Labels")
plt.xlabel("X value")
plt.ylabel("Y value")

plt.show()

# Practice: Change font size of the title using `fontsize` parameter.
