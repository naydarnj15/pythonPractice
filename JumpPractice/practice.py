smallest = None
for interval in [3,4,5,6,6,44,73]:
	if smallest is None or interval < smallest:
		smallest = interval
print('Smallest:', smallest)

largest = None
for interval in [3,4,5,6,6,44,73]:
	if largest is None or interval < largest:
		largest = interval
print('Largest:', largest)


