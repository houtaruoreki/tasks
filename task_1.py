inputs = [len(input(f"enter text {i}:")) for i in range(1,6)]

longest = inputs[0]

for i in inputs:
    if i > longest:
        longest = i
print(longest)
