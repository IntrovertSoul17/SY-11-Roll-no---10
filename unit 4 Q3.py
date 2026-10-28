import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employee.csv")

print("Employee Details:")
print(df[["Name", "Department", "Salary"]])

avg = df.groupby("Department")["Salary"].mean()

print("\nAverage Salary by Department:")
print(avg)

avg.plot(kind="bar")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.title("Employee Salary Analysis")
plt.show()
