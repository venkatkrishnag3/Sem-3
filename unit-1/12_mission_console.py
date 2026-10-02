# Program to simulate an interactive mission console for sensor readings and alerts.

THRESHOLD = 70.0
readings = []

while True:
    print("\n1-add reading 2-report 3-quit")
    choice = input("choice: ").strip()

    if choice == "1":
        val = float(input("Sensor value: "))
        readings.append(val)
    elif choice == "2":
        if not readings:
            print("no data yet")
            continue
        alerts = 0
        for r in readings:
            if r > THRESHOLD:
                alerts += 1
        avg = sum(readings) / len(readings)
        print(f"count = {len(readings)}  avg = {avg:.1f}  alerts = {alerts}")
    elif choice == "3":
        print("mission console closed")
        break
    else:
        print("invalid choice")

# Output:
# 1-add reading 2-report 3-quit
# choice: 1
# Sensor value: 65.5
# 
# 1-add reading 2-report 3-quit
# choice: 1
# Sensor value: 82.0
# 
# 1-add reading 2-report 3-quit
# choice: 2
# count = 2  avg = 73.8  alerts = 1
# 
# 1-add reading 2-report 3-quit
# choice: 3
# mission console closed
