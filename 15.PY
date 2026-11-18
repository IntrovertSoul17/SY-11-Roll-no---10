
import gc

# Check garbage collection status
print("Garbage Collection Enabled:", gc.isenabled())

# Get garbage collection threshold
print("GC Threshold:", gc.get_threshold())

# Create a class
class Demo:
    def __init__(self, name):
        self.name = name

# Create circular references
obj1 = Demo("Object 1")
obj2 = Demo("Object 2")

obj1.ref = obj2
obj2.ref = obj1

print("Objects created with circular references")

# Delete references
del obj1
del obj2

print("Objects deleted")

# Manually run garbage collection
collected = gc.collect()

print("Garbage collected objects:", collected)

# Check garbage collection status
print("GC Enabled:", gc.isenabled())

print("Current GC Count:", gc.get_count())

print("Program completed")
