times = [61709066]
distances = [643118413621041]

ret = 1
for time, distance in zip(times, distances):
    ret *= len([
        1 for i in range(time) if i * (time - i) > distance
    ])
print(ret)
