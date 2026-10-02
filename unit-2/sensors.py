# Program defining sensor helper functions and self-test block.

THRESHOLD = 70.0

def is_alert(value):
    return value > THRESHOLD

def average(values):
    return sum(values) / len(values)

if __name__ == '__main__':
    print("self-test:", is_alert(85), average([10, 20, 30]))

# Output:
# self-test: True 20.0
