import statistics as stats

numbers = [6, 4, 2, 3, 4, 5, 6, 7]
lowest = min(numbers)
highest = max(numbers)
print(lowest, highest)

average = stats.mean(numbers)
stdev = stats.stdev(numbers)
median = stats.median(numbers)
print(average, stdev, median)
