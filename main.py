from calendar import weekheader
from enum import unique
import peewee
from datetime import datetime

database = peewee.MySQLDatabase('python_db', host='localhost', port=3306, user='root', passwd='')

# Users
class User(peewee.Model):
    username = peewee.CharField(max_length=50, unique=True, index=True)
    email = peewee.CharField(max_length=60, null=False)
    active = peewee.BooleanField(default=False)
    created_at = peewee.DateTimeField(default=datetime.now)

    class Meta:
        database = database
        db_table = 'users'


if __name__ == '__main__':
    
    if User.table_exists():
        User.drop_table()

    User.create_table()

    # # Insertando registro mediante el método save()
    # user1 = User(username='rafa', email='rafa@mail.com', active=True)
    # user1.save()

    # #Otra forma de insertar registros
    # user2 = User()
    # user2.username = "user2"
    # user2.email = "user2@mail.com"
    # user2.save()

    # # Otra forma de insertar registros haciendo uso de diccionarios
    # values = {
    #     'username': 'user3',
    #     'email': 'user3@mail.com'
    # }

    # user3 = User(**values)
    # user3.save()


    # # Insertando registros mediante el método create()
    # user4 = User.create(username='user4', email='user4@mail.com')
    # print(user4.id)


    # # Insertando registros mediante el método insert(), este método devuelve un objeto de tipo query
    # query = User.insert(username='user5', email='user5@mail.com')
    # query.execute()


    # Insertando múltiples registros
    users = [
        {'username': 'user1', 'email': 'user1@mail.com', 'active': True},
        {'username': 'user2', 'email': 'user2@mail.com'},
        {'username': 'user3', 'email': 'user3@mail.com', 'active': True},
        {'username': 'user4', 'email': 'user4@mail.com'},
        {'username': 'user5', 'email': 'user5@mail.com'},
        {'username': 'user6', 'email': 'user6@mail.com', 'active': True},
        {'username': 'user7', 'email': 'user7@mail.com', 'active': True},
    ]

    query2 = User.insert_many(users)
    query2.execute()


    # Obteniendo registros

    # El método select() puede recibir como parámetros las columnas que queremos mostrar.
    # Si no recibe parámtros, este método devolverá todas las columnas que tenga la tabla.
    # users = User.select(User.username, User.email)


    # # Obtener registros usando la cláusula where
    # users = User.select(User.username, User.email, User.active).where((User.active == True) & (User.id > 3))

    # for user in users:
    #     print(user.username)


    # # Order by
    # users = User.select().where(User.active == True).order_by(User.username.desc()).limit(2)

    # print(users)

    # for user in users:
    #     print(user.username)


    # # Registros únicos con métodos get() first()
    # try:
    #     user = User.select().where(User.username == 'user11').get()

    #     print(type(user))
    #     print(user)
    # except User.DoesNotExist as err:
    #     print("No fue posible obtener el usuario.")

    # # first()
    # user = User.select().where(User.username == 'user11').first()
    # if user:
    #     print(user)
    # else:
    #     print("No fue posible obtener el usuario.")


    # # Validar registros
    # # Método count()
    # count = User.select().where(User.username == 'user7').count()
    # if count > 0:
    #     print("El usuuario existe en la tabla.")
    # else:
    #     print("No fue posible obtener el usuario.")

    # #Método exists()
    # exists = User.select().where(User.username == 'user7').exists()
    # if exists:
    #     print("El usuuario existe en la tabla.")
    # else:
    #     print("No fue posible obtener el usuario.")


    # # Actualizar registros
    # user = User.select().where(User.id == 1).get()
    
    # user.username = "Nuevo username"
    # user.email = "nuevo_email@correo.com"

    # user.save()

    # # Otra forma de actualizar registros
    # query3 = User.update(username='User2 nuevo valor', email='user2_nuevoemail@correo.com').where(User.id == 2)
    # query3.execute()


    # Eliminar registros
    # Primera forma
    user = User.select().where(User.username == 'user7').get()
    user.delete_instance()

    # Segunda forma
    query4 = User.delete().where(User.id == 6)
    query4.execute()