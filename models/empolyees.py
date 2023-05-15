from config.db import meta
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String


empolyees = Table(
    'empolyees',meta,
    Column('id',Integer,primary_key=True),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('age',Integer),
    Column('country',String(255)),
    Column('position',String(255)),
    Column('salary',Integer),
)