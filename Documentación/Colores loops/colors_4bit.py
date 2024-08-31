print("\033c") # Limpia la terminal

# Reset
RESET = '\033[0;39;49m'

# Colores de alta intensidad
hi_black='\033[0;90m'       # Black
hi_red='\033[0;91m'         # Red
hi_green='\033[0;92m'       # Green
hi_yellow='\033[0;93m'      # Yellow
hi_blue='\033[0;94m'        # Blue
hi_purple='\033[0;95m'      # Purple
hi_cyan='\033[0;96m'        # Cyan ###
hi_white='\033[0;97m'       # White

# Backgrounds de alta intensidad
bg_hi_black='\033[0;100m'   # Black
bg_hi_red='\033[0;101m'     # Red
bg_hi_green='\033[0;102m'   # Green
bg_hi_yellow='\033[0;103m'  # Yellow
bg_hi_blue='\033[0;104m'    # Blue
bg_hi_purple='\033[0;105m'  # Purple
bg_hi_cyan='\033[0;106m'    # Cyan ####
bg_hi_white='\033[0;107m'   # White

diccionario_estilos = {
    'reset': 0,
    'bold': 1,
    'Faint': 2,
    'italic': 3,
    'Underline': 4,
    'slow_blink': 5,
    'rapid_blink': 6,
    'invert': 7,
    'hide': 8,
    'strike': 9,
    'double_underline': 21,
    'Overlined': 53
}


#### TODOS LOS COLORES CON ESTILO EN COLUMNAS 4-BIT
def all_4bit_colors_and_styles(styles=False):
    """
    Generates a formatted string displaying all 4-bit colors.
    Optionally, it can also display various text styles applied to these colors.
    Args:
        styles (bool, optional): If True, the function will display text styles (e.g., bold, underline) applied to the colors. Defaults to False.
    Returns:
        str: A string containing all 4-bit colors, with optional styles applied, ready to be printed as a demo.
    """
    output = []
    colores = [code for code in range(90,100) if code != 98]
    line = [f'\033[0;{color_code}mColor: {str(color_code).rjust(3)}{RESET}' for color_code in colores] # ['\033[0;90mColor: {n}','\033[0;91mColor: {n}','\033[0;92mColor: {n}'...]
    output.append(' | '.join(line)) # ['\033[0;90mColor: {n} | \033[0;91mColor: {n} | \033[0;92mColor: {n} | ...']
    if styles:
        for style_code in diccionario_estilos.values():
            line = [f'\033[{style_code};{color_code}mEstilo: {str(style_code).rjust(2)}{RESET}' for color_code in colores]
            output.append(' | '.join(line))
    output.append('')  # Salto de línea entre bloques
    return '\n'.join(output)

#### TODOS LOS BACKGROUND CON ESTILO EN COLUMNAS 4-BIT
def all_4bit_bg_colors_and_styles(styles=False):
    """
    Generates a formatted string displaying all 4-bit background colors.
    Optionally, it can also display various text styles applied to these background colors.
    Args:
        styles (bool, optional): If True, the function will display text styles (e.g., bold, underline) applied to the background colors. Defaults to False.
    Returns:
        str: A string containing all 4-bit background colors, with optional styles applied, ready to be printed as a demo.
    """
    output = []
    bg_colors = [code for code in range(100,110) if code != 108]
    line = [f'\033[0;{bg_code}mColor: {str(bg_code).rjust(3)}{RESET}' for bg_code in bg_colors]
    output.append(' | '.join(line))
    if styles:
        for style_code in diccionario_estilos.values():
            line = [f'\033[{style_code};{bg_code}mEstilo: {str(style_code).rjust(2)}{RESET}' for bg_code in bg_colors]
            output.append(' | '.join(line))
    output.append('')
    return '\n'.join(output)



if __name__ == '__main__':
    colors_1 = all_4bit_colors_and_styles(styles=True)
    print(colors_1)
    #bg_colors_1 = all_4bit_bg_colors_and_styles(styles=True)
    #print(bg_colors_1)