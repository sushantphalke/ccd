import random
import sys
min_value = 1 
max_value = sys.maxsize
max_value = 500000
random_integers = [random.randint(min_value, max_value) for _ in range(1000)]

with open('random_integers.txt', 'w') as file:
    for num in random_integers:
        file.write(f"{num}\n")

print("Random integers have been written to 'random_integers.txt'")
