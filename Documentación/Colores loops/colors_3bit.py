# Reset
RESET = '\x1b[0;39;49m'

# Colores regulares
black='\x1b[0;30m'        # Black
red='\x1b[0;31m'          # Red
green='\x1b[0;32m'        # Green
yellow='\x1b[0;33m'       # Yellow
blue='\x1b[0;34m'         # Blue
purple='\x1b[0;35m'       # Purple
cyan='\x1b[0;36m'         # Cyan
white='\x1b[0;37m'        # White

# Background
bg_black='\x1b[40m'       # Black
bg_red='\x1b[41m'         # Red
bg_green='\x1b[42m'       # Green
bg_yellow='\x1b[43m'      # Yellow
bg_blue='\x1b[44m'        # Blue
bg_purple='\x1b[45m'      # Purple
bg_cyan='\x1b[46m'        # Cyan
bg_white='\x1b[47m'       # White

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

print('\x1bc') # Limpia la terminal

#### TODOS LOS COLORES CON ESTILO EN COLUMNAS 3-BIT
def all_3bit_colors_and_styles(styles=False) -> str:
    """
    Generates a formatted string displaying all 3-bit colors.
    Optionally, it can also display various text styles applied to these colors.
    Args:
        styles (bool, optional): If True, the function will display text styles (e.g., bold, underline) applied to the colors. Defaults to False.
    Returns:
        str: A string containing all 3-bit colors, with optional styles applied, ready to be printed as a demo.
    """
    output = [] # List to store the output lines
    colors = [code for code in range(30,40) if code != 38] # List comprehensions to fill with all colors code except number 38 | [30,31,32...]
    # Create a line with colors
    line = [f'\x1b[0;{color_code}mColor: {str(color_code).rjust(3)}{RESET}' for color_code in colors] # List comprehensions to fill with each color using de colors list | ['\x1b[0;30mTexto','\x1b[0;31mTexto'...]
    output.append(' | '.join(line)) # Converting the line list into a string and added it to a output list ['\x1b[0;30mTexto | \x1b[0;30mTexto...']
    # Apply styles if styles=True adding one line for each style with different color
    if styles:
        for style_code in diccionario_estilos.values():
            # Each line will represent a col with a color and a different style
            line = [f'\x1b[{style_code};{color_code}mEstilo: {str(style_code).rjust(2)}{RESET}' for color_code in colors]
            output.append(' | '.join(line))
    output.append('')  # New line at the end of the output to separate blocks
    return '\n'.join(output) # Join all lines and return the final string



#### TODOS LOS BACKGROUND CON ESTILO EN COLUMNAS 3-BIT
def all_3bit_bg_colors_and_styles(styles=False) -> str:
    """
    Generates a formatted string displaying all 3-bit background colors.
    Optionally, it can also display various text styles applied to these background colors.
    Args:
        styles (bool, optional): If True, the function will display text styles (e.g., bold, underline) applied to the background colors. Defaults to False.
    Returns:
        str: A string containing all 3-bit background colors, with optional styles applied, ready to be printed as a demo.
    """
    output = []
    bg_colors = [code for code in range(40,50) if code != 48]
    line = [f'\x1b[0;{bg_code}mColor: {str(bg_code).rjust(3)}{RESET}' for bg_code in bg_colors]
    output.append(' | '.join(line))
    if styles:
        for style_code in diccionario_estilos.values():
            line = [f'\x1b[{style_code};{bg_code}mEstilo: {str(style_code).rjust(2)}{RESET}' for bg_code in bg_colors]
            output.append(' | '.join(line))
    output.append('')
    return '\n'.join(output)


if __name__ == '__main__':
    color_3bit = all_3bit_colors_and_styles()
    print(color_3bit)
    #bg_3bit = all_3bit_bg_colors_and_styles()
    #print(bg_3bit)
