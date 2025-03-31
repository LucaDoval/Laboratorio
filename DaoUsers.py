from CursorPool import CursorPool
from User import User
from logger import log
from encryption import encrypt_password


class UserDAO:

    _SELECT = 'SELECT * FROM database ORDER BY id_user'
    _INSERT = 'INSERT INTO database(username, email, password) VALUES(%s, %s, %s)'
    _UPDATE = 'UPDATE database SET username=%s, email=%s, password=%s WHERE id_user=%s'
    _DELETE = 'DELETE FROM database WHERE id_user=%s'

    @classmethod
    def select(cls):
        with CursorPool() as curs:
            curs.execute(cls._SELECT)
            records = curs.fetchall()
            data = []
            for record in records:
                username = User(record[0], record[1], record[2])
                data.append(username)

            return data

    @classmethod
    def insert(cls, usercls):

        with CursorPool() as curs:
            try:
                # encripto la contraseña que voy a ingresar a la base de datos antes de pasarla como valor
                hashed = encrypt_password(usercls.password)
                values = (usercls.username, usercls.email, hashed)
                # ejecuto la sentencia
                curs.execute(cls._INSERT, values)
                # Verifico que la insercion fue exitosa
                log.debug(f'Usuario agregado: {usercls}')
                return curs.rowcount
            except Exception as e:
                log.debug(f'Error al autenticar usuario: {str(e)}')
                return False

    @classmethod
    def update(cls, data):
        with CursorPool() as curs:
            try:
                hashed = encrypt_password(data.password)
                values = (data.username, data.email, hashed, data.id_user)
                curs.execute(cls._UPDATE, values)
                log.debug(f'Usuario Actualizado: {data}')
                return curs.rowcount
            except Exception as e:
                log.debug(f'No se pudo actualizar el usuario: {e}')
                return False

    @classmethod
    def delete(cls, data):
        with CursorPool() as curs:
            values = data.id_user
            curs.execute(cls._DELETE, values)
            log.debug(f'Usuario eliminado: {data}')
            return curs.rowcount


if __name__ == '__main__':

    # Insert()

    # user1 = User(username='', email='lucadoval1@gmail.com', password='Camila')
    # insert = UserDAO.insert(user1)
    # log.debug(f'Usuario agregado: {insert}')
    #
    # Select()

    users = UserDAO.select()
    for user in users:
      log.debug(user)

    # Update Data

    # user2 = User(2, 'Camila', 'camilalbite@gmail.com', 'latenesadentrojulian')
    # update_data = UserDAO.update(user2)
    # log.debug(f'Dato actualizado: {update_data}')

    # Delete()
    # person1 = Person(id_person=16)
    # delete_data = PersonDAO.delete(person1)
    # log.debug(f'Dato eliminado: {delete_data}')