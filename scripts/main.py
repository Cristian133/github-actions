import os

# Leer el secret desde la variable de entorno
secret_key = os.getenv('MY_SECRET_KEY')

if secret_key:
    print("Secret key loaded successfully!")
else:
    print("Failed to load secret key.")

