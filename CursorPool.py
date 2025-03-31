from logger import log
from Connection import Connection


class CursorPool:

    def __init__(self):
        self._connection = None
        self._cursor = None

    # Obtengo la conexion
    def __enter__(self):
        log.debug('Inicio del metodo with __enter__')
        self._connection = Connection.getConnection()
        self._cursor = self._connection.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        log.debug('Se ejecuta el metodo __exit__')
        if exc_val:
            self._connection.rollback()
            log.debug(f'Ocurrio una excepcion: {exc_tb} {exc_val} {exc_tb}')
        else:
            self._connection.commit()
            log.debug('Se realizo correctamente el commit')
        self._cursor.close()
        Connection.releaseConnection(self._connection)