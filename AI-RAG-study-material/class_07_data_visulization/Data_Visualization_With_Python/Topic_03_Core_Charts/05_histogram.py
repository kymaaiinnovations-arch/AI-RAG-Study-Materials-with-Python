"""
Histogram lesson

Definition: Histograms show distribution of numeric data.
Why: To see frequency of values in ranges (bins).
Real-world Example: Distribution of student marks.
Installation: `pip install matplotlib`
File: 05_histogram.py
"""

import matplotlib.pyplot as plt

marks = [50,55,60,65,70,75,80,85,90,95]

plt.hist(marks, bins=5, color='lightblue', edgecolor='black')
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

# Expected Output: A histogram showing how marks are distributed across bins.

# Practice: Increase bin count to see finer detail.
