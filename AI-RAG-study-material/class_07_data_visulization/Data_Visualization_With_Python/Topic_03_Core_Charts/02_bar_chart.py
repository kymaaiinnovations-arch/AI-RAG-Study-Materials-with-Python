"""
Bar Chart lesson

Definition: Bar charts compare categories.
Why: To compare values across discrete categories.
Real-world Example: Student marks across subjects.
Installation: `pip install matplotlib`
File: 02_bar_chart.py
"""

import matplotlib.pyplot as plt

subjects = ["Math", "Science", "English"]
marks = [80, 90, 75]

plt.bar(subjects, marks, color=['skyblue', 'lightgreen', 'salmon'])
plt.title("Student Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()

# Expected Output: A bar chart with three colored bars.

# Practice: Add numerical labels on top of each bar.
