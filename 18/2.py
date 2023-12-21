x, y, area = 0, 0, 2
with open('1.2.in') as file:
    for line in file:
        _, _, color = line[:-1].split(' ')
        length = int(color[2:7], 16)
        area += length
        match color[7]:
            case '2':
                x -= length
                area -= length * y * 2
            case '0':
                x += length
                area += length * y * 2
            case '3':
                y += length
            case '1':
                y -= length
print(area // 2)
