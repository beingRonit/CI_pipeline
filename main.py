import matplotlib.pyplot as plt
import random2 as randm  # Use random2 for Python 2 compatibility
import os

# Generate random data
categories = ['Cat', 'Dog']
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
data = {category: [randm.randint(5, 20) for _ in days] for category in categories}

# Bar Chart
plt.figure(figsize=(10, 5))
x = range(len(days))
bar_width = 0.35

plt.bar([i - bar_width/2 for i in x], data['Cat'], width=bar_width, label='Cat', color='skyblue')
plt.bar([i + bar_width/2 for i in x], data['Dog'], width=bar_width, label='Dog', color='salmon')

plt.xlabel('Day')
plt.ylabel('Count')
plt.title('Bar Chart: Random Count of Cats and Dogs per Day')
plt.xticks(x, days)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

# Save bar chart
bar_chart_path = os.path.join(os.getcwd(), 'bar_chart.png')
plt.savefig(bar_chart_path)
plt.close()

# Line Chart
plt.figure(figsize=(10, 5))
plt.plot(days, data['Cat'], marker='o', label='Cat', color='skyblue')
plt.plot(days, data['Dog'], marker='s', label='Dog', color='salmon')

plt.xlabel('Day')
plt.ylabel('Count')
plt.title('Line Chart: Random Count of Cats and Dogs per Day')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save line chart
line_chart_path = os.path.join(os.getcwd(), 'line_chart.png')
plt.savefig(line_chart_path)
plt.close()

print("Charts saved as:")
print(bar_chart_path)
print(line_chart_path)
