import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/warehouse_data.csv')

# Summary stats
print("Summary Statistics:")
print(df.describe())

# Errors by department
errors = df.groupby('department')['errors'].sum()
print("\nErrors by Department:")
print(errors)

# Plot errors
errors.plot(kind='bar', title='Total Errors by Department')
plt.xlabel('Department')
plt.ylabel('Errors')
plt.savefig('visuals/errors_by_department.png')
plt.show()

# Average delay
avg_delay = df.groupby('department')['delay_minutes'].mean()
print("\nAverage Delay by Department:")
print(avg_delay)
