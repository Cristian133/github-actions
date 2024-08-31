import os

# Leer el secret desde la variable de entorno
secret_key = os.getenv('MY_SECRET_KEY')
variable = os.getenv('ALIEN')

print("Hola mundo python")
print(f"Secret key loaded successfully!{secret_key}")
print(f"Variable key loaded successfully!{variable}")

