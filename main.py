"""
ORM - (OBJECT RELATOINAL MAPPING) - объектно реалиционное отображение
Технология которая связывает БД с консепциями объектно ориентированных языков программиорвания,
ORM -  прослойка между Бд и кодом который пишет программист ,
которая позволяет создавать в программе объекты обновлять,
удалять получать их.


python:
    peewee
    sqlalchemy
    DjangoORM

Класс - тааблица в БД
Аттрибут класса - пооле в БД
ОБъект класаа - строка в таблице


"""
# нужно создать виртуальное окружение (venv) - обязательно!


from settings import db
from views import *

db.connect()
get_categories()
get_products()
