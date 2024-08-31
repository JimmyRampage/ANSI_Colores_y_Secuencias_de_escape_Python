RESET = '\033[0m'
MAGENTA = '\033[35m'

def highlight_keyword(text, keyword):
    highlighted = text.replace(keyword, f"{MAGENTA}{keyword}{RESET}")
    print(highlighted)

highlight_keyword("El lenguaje de programación Python es poderoso y fácil de aprender.", "Python")