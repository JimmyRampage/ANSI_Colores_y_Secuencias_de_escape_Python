# Función para colorear con 3-4-bit

def print_color_text(color_name :str,text :str) -> str:

    # Para evitar conflicto por aA
    color_name.lower()
    # Diccionario de colores de código 30-37
    colors = {
    'black':'\033[0;30m',
    'red':'\033[0;31m',
    'green':'\033[0;32m',
    'yellow':'\033[0;33m',
    'blue':'\033[0;34m',
    'purple':'\033[0;35m',
    'cyan':'\033[0;36m',
    'white':'\033[0;37m',
    }
    reset = '\x1b[0m'
    print(colors.get(color_name, '') + text + reset)

print_color_text('red', 'Texto Rojo')
print_color_text('blue', 'Texto Azul')
print_color_text('cyan', 'Texto Cyan')