from sqlalchemy import *

from model.models import Comentario, Usuario, Publicacao, Curtida

engine = create_engine("mysql+pymysql://root@localhost:3306/python")

Usuario.__table__.create(engine, checkfirst=True)
Publicacao.__table__.create(engine, checkfirst=True)
Comentario.__table__.create(engine, checkfirst=True)
Curtida.__table__.create(engine, checkfirst=True)