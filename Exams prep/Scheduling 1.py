from collections import deque

jobs = deque(map(int, input().split(', ')))
job_index = int(input())

clock_cycles = 0
job = jobs[job_index]

for el in jobs:
    if el <= job:
        clock_cycles += el


print(clock_cycles)
