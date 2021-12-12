from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from model.models import Usuario, Publicacao, Comentario, Curtida

listakm = []
engine = create_engine("mysql+pymysql://root@localhost:3306/python")


Session = sessionmaker(bind=engine)
session = Session()

def createuser(email1, senha1):
    user = Usuario(email=email1, senha=senha1)
    # Adiciona o objeto na session
    session.add(user)
    # Executa a operacao no banco e atualiza o objeto
    session.commit()

def createpubli(datahorainicial, datahora_final, kms, atividadetipo, lugar, iduser):
    publi = Publicacao(datahora_inicio = datahorainicial, datahora_fim = datahora_final, quilometros = kms, tipo_atividade = atividadetipo, local = lugar, usuario_id = iduser )
    session.add(publi)
    session.commit()

def comentar(iduser, idpubli, comentario1):
    comentar = Comentario(comentario = comentario1, usuario_id = iduser, publicacao_id = idpubli)
    session.add(comentar)
    session.commit()

def curtir(iduser, idpubli):
    curtir = Curtida(usuario_id = iduser, publicacao_id = idpubli )
    session.add(curtir)
    session.commit()

def infopubli():
    # SELECT * FROM Usuario ORDER BY id
    tuplas = session.query(Publicacao).order_by(Publicacao.local)
    for tupla in tuplas:
        print(tupla.usuario_id, "-", tupla.quilometros, "KMs - Início ", tupla.datahora_inicio, " - Fim",tupla.datahora_fim)
        listakm.append(tupla.quilometros)
    
    print("\nQuilometragem crescente: {}".format(sorted(listakm)))

def trocarsenha(useremail, novasenha):
    user = Usuario.find_by_email(session=session, email=useremail)
    user.senha = novasenha
    session.commit()

def deletarvga(useremail):
    userid = session.query(Usuario).filter_by(email=useremail).first()
    session.delete(Usuario).filter(Usuario.id == userid.id).filter(Publicacao.id=="VGA")
    

    session.commit()

#2
createuser("usu1@usu.com", "123abc")
createuser("usu2@usu.com", "321abc")
createuser("usu3@usu.com", "abc123")

#3
createpubli("2021-01-07 15:00:00", "2021-01-07 15:30:00", 2.7, "Caminhada", "VGA", 6)
createpubli("2021-01-13 12:30:00", "2021-01-13 13:00:00", 1.5, "Caminhada", "VGA", 6)
createpubli("2021-01-07 15:00:00", "2021-01-07 16:00:00", 6.0, "Corrida", "SP", 6)
createpubli("2021-01-07 16:00:00", "2021-01-07 17:00:00", 2.7, "Caminhada", "VGA", 7)
createpubli("2021-01-13 06:30:00", "2021-01-13 07:30:00", 2.9, "Caminhada", "VGA", 7)
createpubli("2021-01-07 13:00:00", "2021-01-07 15:00:00", 12.0, "Corrida", "SP", 7)
createpubli("2021-01-07 14:00:00", "2021-01-07 14:30:00", 2.5, "Caminhada", "VGA", 8)
createpubli("2021-01-13 11:00:00", "2021-01-13 12:00:00", 3.0, "Caminhada", "VGA", 8)
createpubli("2021-01-07 17:00:00", "2021-01-07 18:00:00", 6.0, "Caminhada", "SP", 8)

#4
comentar(7, 5, "Boa!")
comentar(6, 6, "Parabéns!")
comentar(7, 8, "Legal!")
comentar(8, 8, "Boa!")

#5
curtir(6, 8)
curtir(6, 9)
curtir(6, 10)
curtir(6, 11)
curtir(6, 12)
curtir(6, 13)
curtir(7, 5)
curtir(7, 6)
curtir(7, 7)
curtir(7, 11)
curtir(7, 12)
curtir(7, 13)
curtir(8, 5)
curtir(8, 6)
curtir(8, 7)
curtir(8, 8)
curtir(8, 9)
curtir(8, 10)

#6 - 6.a)
infopubli()

#7
trocarsenha("usu1@usu.com", "senhausu1")

#8
deletarvga("usu2@usu.com")