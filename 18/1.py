x, y, area = 0, 0, 1
with open('1.2.in') as file:
    for line in file:
        direction, length, color = line[:-1].split(' ')
        length = int(length)
        area += length / 2
        match direction:
            case 'L':
                x -= length
                area -= length * y
            case 'R':
                x += length
                area += length * y
            case 'U':
                y += length
            case 'D':
                y -= length
print(area)
