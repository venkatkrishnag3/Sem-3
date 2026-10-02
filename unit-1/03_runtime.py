# Program to calculate estimated runtime from battery capacity and current draw.

capacity = float(input("Enter battery capacity (mAh): "))
current = float(input("Enter current drawn (mA): "))

runtime = capacity / current
print(f"Estimated runtime: {runtime:.2f} hours")

# Output:
# Enter battery capacity (mAh): 3000
# Enter current drawn (mA): 450
# Estimated runtime: 6.67 hours
