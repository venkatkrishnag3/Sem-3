# Program to demonstrate importing modules, namespaces, and checking __name__.

import sensors
from sensors import is_alert
import sensors as sn

readings = [62, 84, 71]
print("threshold:", sensors.THRESHOLD)
print("average:", sensors.average(readings))

for r in readings:
    status = "ALERT" if sensors.is_alert(r) else "ok"
    print(r, "->", status)

print("__name__ inside main.py is:", __name__)
print("__name__ inside sensors.py is:", sensors.__name__)

print("is_alert(85):", is_alert(85))
print("sn.is_alert(85):", sn.is_alert(85))

# Output:
# threshold: 70.0
# average: 72.33333333333333
# 62 -> ok
# 84 -> ALERT
# 71 -> ALERT
# __name__ inside main.py is: __main__
# __name__ inside sensors.py is: sensors
# is_alert(85): True
# sn.is_alert(85): True
