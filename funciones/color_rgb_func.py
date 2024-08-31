# Función para colorear con 24-bit rgb

def print_color_text_rgb(r:int,g:int,b:int,text :str) -> str:

    # Diccionario de colores de código 30-37
    reset = '\x1b[0m'
    color = f'\x1b[38;2;{r};{g}:{b}m'
    print(color + text + reset)

if __name__ == '__main__':

    print_color_text_rgb(220,0,0, 'Texto Rojo')
    print_color_text_rgb(64,128,224, 'Texto Azul')
    print_color_text_rgb(224,128,0, 'Texto Naranjo')