"""
Pie Chart lesson

Definition: Pie charts show parts of a whole.
Why: To visualise proportions.
Real-world Example: Language usage share in a project.
Installation: `pip install matplotlib`
File: 04_pie_chart.py
"""

import matplotlib.pyplot as plt

sizes = [40, 35, 25]
labels = ["Python", "Java", "C++"]

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title("Language Usage")
plt.axis('equal')  # Equal aspect ratio ensures pie is drawn as a circle.

plt.show()

# Expected Output: A pie chart with percentage labels.

# Practice: Explode the largest slice slightly.
