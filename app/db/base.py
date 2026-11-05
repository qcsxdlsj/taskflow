# from sqlalchemy.orm import DeclarativeBase


# class Base(DeclarativeBase):
#     """所有 ORM 模型的基类。

#     每个模型类都继承它，SQLAlchemy 就会把这些类的信息
#     收集到 Base.metadata 里，建表和迁移都靠这个 metadata。
#     """

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    '''111'''
