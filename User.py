from logger import log


class User:

    def __init__(self, id_user=None, username=None, email=None, password=None):
        self._id_user = id_user
        self._username = username
        self._email = email
        self._password = password

    @property
    def id_user(self):
        return self._id_user

    @id_user.setter
    def id_user(self, id_user):
        self._id_user = id_user

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username
        
    @property
    def email(self):
        return self._email 
    
    @email.setter
    def email(self, email):
        self._email = email

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __str__(self):
        return (f"""
                id_user = {self._id_user}
                username = {self._username}
                Email = {self._email}
                password = {self._password}
                """)


if __name__ == '__main__':
    person1 = User(id_user=1, username='Anakin', email='elElegido@gmail.com', password='JodeteMaceWindu')
    log.debug(person1)
