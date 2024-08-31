
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'

def log(message, level):
    if level == "info":
        print(f"{GREEN}[INFO] {message}{RESET}")
    elif level == "warning":
        print(f"{YELLOW}[WARNING] {message}{RESET}")
    elif level == "error":
        print(f"{RED}[ERROR] {message}{RESET}")

log("El sistema está iniciando.", "info")
log("Espacio en disco bajo.", "warning")
log("No se pudo conectar a la base de datos.", "error")