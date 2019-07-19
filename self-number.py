# d(91)=9+1+91=101
# n : d(n)'s generator
# 91, 10 : 101's generator
# If number has not any generator, it called self-number
# {} : sets
# Find the sum of the self-number from 1 to 5000

print(sum(set(range(1, 5000)) - {n + sum((int(i) for i in str(n))) for n in range(1, 5000)}))
