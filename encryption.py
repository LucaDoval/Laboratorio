import bcrypt


def encrypt_password(password):
    # genero un "sal" aleatorio
    # sal >> cadena aleatoria que se concatena con la contraseña para mejorar su encriptacion
    salt = bcrypt.gensalt()
    # encripto la contraseña
    hash_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hash_password


def check_password(password, hashed_password):
    # Chequeo de la contraseña
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return f'La contraseña es correcta:  {print(password)}'
    else:
        return 'Contraseña incorrecta'