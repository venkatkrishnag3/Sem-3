# Program to demonstrate local and global variable scope in Python.

THRESHOLD = 70

def is_alert(value):
    return value > THRESHOLD

print("alert check:", is_alert(85), is_alert(60))

count = 0

def tick():
    global count
    count += 1
    return count

print("tick:", tick(), tick(), tick())
print("global count is now:", count)

def tick_param(val):
    return val + 1

c = 0
c = tick_param(c)
print("functional count:", c)

# Output:
# alert check: True False
# tick: 1 2 3
# global count is now: 3
# functional count: 1
