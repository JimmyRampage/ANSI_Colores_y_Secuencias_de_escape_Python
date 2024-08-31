

RESET = '\033[0m'
BLUE = '\033[34m'
PURPLE = '\033[35m'

data = [
    ("Nombre", "Edad", "Ciudad"),
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 35, "Chicago")
]

for index, (name, age, city) in enumerate(data):
    color = BLUE if index % 2 == 0 else PURPLE
    print(f"{color}{name.ljust(10)}{str(age).ljust(5)}{city.ljust(15)}{RESET}")