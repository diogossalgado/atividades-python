from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, DateTime, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import VARCHAR

Base = declarative_base()

class Usuario(Base):
    # indica o nome da tabela no BD
    __tablename__ = 'usuario'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    senha = Column(String(45), nullable=False)

    #nome = Column(String(25))
    #data_inicio = Column(Date)

    # Referencia para as publicacoes do usuario. Exemplo de uso: create2()
    publicacoes = relationship("Publicacao",backref='Usuario', lazy=True)

    '''def __repr__(self):
        return f'Usuario {self.nome}'''

    @classmethod
    def find_by_email(cls, session, email):
        return session.query(cls).filter_by(email=email).one()


# Relacionamento 1:N - Usuário = Várias Publicações 
# Usuario - Classe parent | Publicacao - Classe child

class Publicacao(Base):
    # Indica o nome da tabela no BD
    __tablename__ = 'publicacao'
    id = Column(Integer, Sequence('publica_id_seq'), primary_key=True)
    
    datahora_inicio = Column(DateTime(), nullable = False)
    datahora_fim = Column(DateTime(), nullable = False)

    quilometros = Column(DECIMAL(10, 2), nullable = False)
    tipo_atividade = Column(String(45), nullable = False)
    local = Column(String(255), nullable = False)

    # Cria a chave estrangeira
    usuario_id = Column(Integer, ForeignKey('usuario.id'))

    # ( Opcional ) Criar referencia para o objeto. Exemplo de uso create3()
    usuario = relationship("Usuario", backref="Publicacao")

class Comentario(Base):
   # indica o nome da tabela no BD
    __tablename__ = 'comentario'

    id = Column(Integer, Sequence('comentario_id_seq'), primary_key=True)

    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    publicacao_id = Column(Integer, ForeignKey('publicacao.id'))

    comentario = Column(String(255), nullable = False)
    publicacoes = relationship("Comentario",backref='Usuario', lazy=True)

class Curtida(Base):
    # indica o nome da tabela no BD
    __tablename__ = 'curtida'

    id = Column(Integer, Sequence('curtida_id_seq'), primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    publicacao_id = Column(Integer, ForeignKey('publicacao.id'))

    publicacoes = relationship("Curtida",backref='Usuario', lazy=True)
    publicacoes = relationship("Curtida",backref='Publicacao', lazy=True)



