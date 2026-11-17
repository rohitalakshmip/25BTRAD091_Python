items = input("Enter elements: ").split()

freq = {}

for item in items:
    freq[item] = freq.get(item, 0) + 1

print("Frequency:")
for item, count in freq.items():
    print(item, ":", count)