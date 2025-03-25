import uuid

def get_valid_option(prompt, options):
    while True:
        try:
            value = int(input(prompt))
            if 1 <= value <= len(options):
                return value
            else:
                print(f"Por favor, digite um número entre 1 e {len(options)}.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Por favor, digite um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número decimal (ex: 12.5).")

def calculate_rectangle_area(base, height):
    return base * height

def calculate_triangle_area(base, height):
    return (base * height) / 2

def generate_id():
    return str(uuid.uuid4())