import peewee
database_connection=peewee.MySQLDatabase("hk",user="dbms",password="Gowtham7@",host="")
database_connection.connect()
class User(peewee.Model):
    class Meta:
        database=database_connection
        username=peewee.CharField(primary_key=True)
        password=peewee.CharField()
        name=peewee.CharField()
def authenticate_user(username, password):
        user= User.select().where(User.username==username,User.password==password)
        user.execute()
        return user.exists()