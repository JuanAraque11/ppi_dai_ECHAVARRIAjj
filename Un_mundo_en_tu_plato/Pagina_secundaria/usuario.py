class Usuario:
    def __init__(self, username, contraseña):
        self._username = username
        self._contraseña = contraseña

    def get_username(self):
        return self._username

    def set_username(self, nuevo_username):
        self._username = nuevo_username

    def get_contraseña(self):
        return self._contraseña


    def set_contraseña(self, nueva_contraseña):
        self._contraseña = nueva_contraseña
