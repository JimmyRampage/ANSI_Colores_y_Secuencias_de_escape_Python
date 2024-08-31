print("\033c") # Limpia la terminal

RESET = '\u001b[0m'

# All 24-bit colors
def all_24bit_colors(step=32):
    count = 0
    for r in range(0,256,step):
        for g in range(0,256,step):
            for b in range(0,256,step):
                r_code = str(r).rjust(3)
                g_code = str(g).rjust(3)
                b_code = str(b).rjust(3)
                print(f'\u001b[38;2;{r};{g};{b}m({r_code};{g_code};{b_code}){RESET}',end='\n' if 7 == count%8 else '')
                count += 1

# All 24-bit background colors
def all_24bit_bg_colors(step=32):
    count = 0
    for r in range(0,256,step):
        for g in range(0,256,step):
            for b in range(0,256,step):
                r_code = str(r).rjust(3)
                g_code = str(g).rjust(3)
                b_code = str(b).rjust(3)
                print(f'\u001b[48;2;{r};{g};{b}m({r_code};{g_code};{b_code}){RESET}',end='\n' if 7 == count%8 else f'')
                count += 1

if __name__ == '__main__':
    all_24bit_colors()
    #all_24bit_bg_colors()