

# demo cript.

import bcrypt

# Votre mot de passe de 8 caractères (type 'str')
password = "Test1234"

# 1. Conversion en octets (bytes) via .encode('utf-8')
password_bytes = password.encode('utf-8')

# 2. Génération du 'salt' et hashage
salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password_bytes, salt)

print(hashed_password)


# TODO: make a CRUD user in main file, for try.