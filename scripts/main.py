import os

# Leer el secret desde la variable de entorno
secret_key = os.getenv('MY_SECRET_KEY')
variable = os.getenv('ALIEN')

print(f"Secret key loaded successfully!\n{secret_key}\nSecret key loaded successfully!{variable}")

