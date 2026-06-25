"""
Mini project: Sales dashboard

Definition: Combine line and bar charts to make a simple dashboard.
Why: Practice putting pieces together.
File: 02_sales_dashboard.py
"""

import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]n
sales = [120,150,180,220]
returns = [5,7,6,4]

fig, ax1 = plt.subplots()

ax1.plot(months, sales, color='tab:blue', marker='o', label='Sales')
ax1.set_xlabel('Month')
ax1.set_ylabel('Sales', color='tab:blue')
ax1.tick_params(axis='y', labelcolor='tab:blue')

ax2 = ax1.twinx()
ax2.bar(months, returns, alpha=0.3, label='Returns', color='tab:orange')
ax2.set_ylabel('Returns', color='tab:orange')
ax2.tick_params(axis='y', labelcolor='tab:orange')

plt.title('Sales Dashboard')
fig.tight_layout()
plt.show()

# Practice: Save the dashboard as `dashboard.png` using `fig.savefig()`.
