import os

# Leer el secret desde la variable de entorno
secret_key = os.getenv('MY_SECRET_KEY')

if secret_key:
    print(f"Secret key loaded successfully!\n{secret_key}")
else:
    print("Failed to load secret key.")

