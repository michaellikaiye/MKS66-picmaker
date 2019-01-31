with open("image.ppm", 'w', encoding = 'utf-8') as f:
    width = 500
    height = 500
    maxval = 255
    header = f'P3 {width} {height} {maxval}\n'
    f.write(header)
    i = 0
    zoom = 2000
    for i in range(width):
        for j in range(height):
            R = int(i * j * j / zoom) % 256
            G = int(i * i * j / zoom) % 256
            B = int((i + j) * (i + j) / zoom) % 256
            color = f'{R} {G} {B} '
            f.write(color)
