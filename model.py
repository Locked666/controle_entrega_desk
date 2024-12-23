from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date, ForeignKey, Text, BLOB,Float,Boolean,Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from datetime import datetime,date
from pathlib import Path
from ConfigApp import MODE_DEBUG, PATH_DATABASE
import os 

CONN = f"sqlite:///{PATH_DATABASE}"

engine = create_engine(CONN,echo=MODE_DEBUG)
Session =  sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Parametros(Base):
    __tablename__='parametros'
    id = Column(Integer, primary_key=True, autoincrement=True,default=1)
    script =  Column(Integer, default=0, comment="Número do Script a ser executado")
    log_inclusao = Column(DateTime, default=datetime.now()) 


class CadastroApp(Base):
    __tablename__='cad_aplicativos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome =  Column(String)
    obs = Column(String)
    log_inclusao = Column(DateTime, default=datetime.now()) 

class LancEntrega(Base):
    __tablename__='lanc_entrega'
    id = Column(Integer, primary_key=True, autoincrement=True)
    app = Column(String)
    data_lanc =  Column(Date)
    hora_inicial = Column(Time)
    hora_final = Column(Time)
    qt_hora = Column(Time)
    km_inicial=Column(Float)
    km_final=Column(Float)
    km_total=Column(Float)
    km_lt = Column(Float)
    qt_entregas = Column(Integer)
    vlr_recebido = Column(Float)
    obs = Column(String)
    log_inclusao = Column(DateTime, default=datetime.now()) 


class LancEntregaItens(Base):
    __tablename__='lanc_entrega_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    cod_detalha = Column(Integer)
    entrega_lanc = Column(Integer, ForeignKey('lanc_entrega.id'))
    hora_inicial = Column(Time)
    hora_final = Column(Time)
    qt_hora = Column(Time)
    km_inicial=Column(Float)
    km_final=Column(Float)
    km_total=Column(Float)
    tp_pagamento =  Column(Integer,default=0 ,comment="Index do pagamento")
    vlr_recebido = Column(Float)

    obs = Column(String)
    log_inclusao = Column(DateTime, default=datetime.now())  


class LancAbastecimento(Base):
    __tablename__='lanc_abastecimento'
    id = Column(Integer, primary_key=True, autoincrement=True)
    data_lanc =  Column(DateTime)
    tp_combustivel =  Column(String)
    tp_pagamento =  Column(String)
    km_rodados = Column(Float)
    trip = Column(Float)
    media_lt = Column(Float)
    nome_posto = Column(String)
    vlr_lt = Column(Float, comment="Valor pago por litro")
    qt_abastecido =  Column(Float, comment="Quantidade de litros Abastecidos")
    vlr_total =  Column(Float, comment="Valor total pago pelo abastecimento")
    obs =  Column(String)
    log_inclusao = Column(DateTime, default=datetime.now()) 




if not os.path.exists(PATH_DATABASE):
    Base.metadata.create_all(bind=engine) 


if __name__=='__main__':
    Base.metadata.create_all(bind=engine)
    pass
