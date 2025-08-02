from logger import log
from psycopg2 import pool


class Connection:

    _DATABASE = 'Laboratory'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '<Port>'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def getPool(cls):

        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      host=cls._HOST,
                                                      user=cls._USERNAME,
                                                      password=cls._PASSWORD,
                                                      port=cls._DB_PORT,
                                                      database=cls._DATABASE)
                log.debug(f'Conexion de pool exitosa: {cls._pool}')
                return cls._pool

            except Exception as e:
                log.error(f'Conexion de poll erronea: {e}')

        else:
            return cls._pool

    # Conexion Pool
    @classmethod
    def getConnection(cls):
        connect = cls.getPool().getconn()
        log.debug(f'Conexion establecida: {connect}')
        return connect

    # Liberacion de la conexion
    @classmethod
    def releaseConnection(cls, connection):
        cls.getPool().putconn(connection)
        log.debug(f'Liberacion de la conexion exitosa: {connection}')

    # Cierre de conexiones
    @classmethod
    def closeConnection(cls):
        cls.getPool().closeall()


if __name__ == '__main__':

        connection1 = Connection.getConnection()
        Connection.releaseConnection(connection1)

        connection2 = Connection.getConnection()

        connection3 = Connection.getConnection()
        Connection.releaseConnection(connection3)

        connection4 = Connection.getConnection()
        connection5 = Connection.getConnection()
        connection6 = Connection.getConnection()
        Connection.releaseConnection(connection6)
