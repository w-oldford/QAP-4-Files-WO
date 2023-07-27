# Description: A program that creates a graph of revenue for One Stop Insurance.
# By: Will Oldford
# Date Created: 07-26-23

# libraries
import matplotlib.pyplot as plt

# graph:
x_axis = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = [0,0,0,0,0,0,0,0,0,0,0,0]
num = 0
for Month in x_axis:
    y_axis[num] = int(input(f"Enter Total Revenue From {Month}: "))
    num += 1

plt.plot(x_axis,y_axis,marker="o",markersize=5,)

plt.xlabel("Month")
plt.ylabel("Revenue ($)")

plt.title("Graph of Monthly Revenue")
plt.grid(True)
plt.show()