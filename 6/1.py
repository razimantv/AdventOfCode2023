times = [61, 70, 90, 66]
distances = [643, 1184, 1362, 1041]

ret = 1
for time, distance in zip(times, distances):
    ret *= len([
        1 for i in range(time) if i * (time - i) > distance
    ])
print(ret)
