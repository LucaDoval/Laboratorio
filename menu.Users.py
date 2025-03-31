import DaoUsers as dao
from User import User

# Creo un bucle While True para poder permanecer en el menu excepto que el usuario
# utilize la opcion de cerrar menu (opcion 5).2
while True:
    print('Bienvenido al Menu de Usuario')
    menu = (input("""
                    Menu:
                    1. Lista de Ususarios:
                    2. Agregar usuarios:
                    3. Actualizar usuarios
                    4. Eliminar usuario: 
                    5. Salir
                    
                    Elegi una opcion: 
                    """))
    # Muestra la lista
    if menu == "1":
        users = dao.UserDAO.select()
        for user in users:
            print(user)
    # Agrego a la lista
    elif menu == "2":
        print('Nuevo usuario: ')
        name = input('Nombre: ')
        mail = input('Email: ')
        pwd = input('Contraseña: ')
        values = User(username=name, email=mail, password=pwd)
        data = dao.UserDAO.insert(values)
        print(f'Usuario agregado: {data}')
    # Modifico la lista
    elif menu == "3":
        print('Actualizar usuario:')
        id = int(input('Proporciona el id que quieras actualizar: '))
        name = input('Nuevo nombre: ')
        mail = input('Nuevo email: ')
        pwd = input('Nueva Contraseña: ')
        values = User(id, name, mail, pwd)
        new_data = dao.UserDAO.update(values)
        print(f'Usuario actualizado: {new_data}')
    # Elimino elementos de la lista
    elif menu == "4":
        id_delete = input('Proporciona el ID del usuario que quieras eliminar: ')
        value = User(id_user=id_delete)
        delete_data = dao.UserDAO.delete(value)
        print(f'Usuario eliminado: {delete_data}')
    # Finalizo el Menu de Usuarios
    elif menu == "5":
        print('Cerrando Menu de Usuario...')
        break
    else:
        print('Opcion no valida. Intentelo de vuelta')

