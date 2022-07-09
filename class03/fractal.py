import array

# Con 640 x 480 salen 4 imgs
width = 640
height = 480
max_iteraciones = 255

# Crear imagen en formato PPM
def crearPPM(fractal):
    ppm_header = f'P6 {width} {height} {max_iteraciones}\n'
    image = array.array('B', fractal)

    with open('mandel.ppm', 'wb') as f:
        f.write(bytearray(ppm_header, 'ascii'))
        image.tofile(f)

#Ejecutamos esta funcion para cada punto en el plano complejo, por ejemplo c_x, c_y pueden ser iguales a (0.3, 0.2)
def calcular_punto(c_x, c_y):
    i = 0
    z = complex(0,0)
    while i < max_iteraciones:
        z = z * z + complex(c_x, c_y)
        if abs(z) > 2:
            break
        i = i + 1
    
    return i

def calcular_fractal(x_0, y_0, x_1, y_1):
    fractal = []
    x_step = (x_1 - x_0) / width
    y_step = (y_1 - y_0) / height

    for i in range(0, width):
        for j in range(0, height):
            #print("x_0: ", x_0, ", i: ", i, " x_step: ", x_step, "y_0: ", y_0, ", j: ", j, " y_step: ", y_step)
            fractal.append(calcular_punto(x_0 + i * x_step, y_0 + j * y_step))

    return fractal

if __name__ == "__main__":
    fractal = calcular_fractal(-1.5, -1, 1, 1)
    crearPPM(fractal)   