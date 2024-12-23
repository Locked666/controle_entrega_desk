from model import CadastroApp,LancEntrega,LancEntregaItens,LancAbastecimento, CONN, Base,engine,session
from sqlalchemy.schema import CreateTable
from sqlalchemy import func,text,inspect, create_engine, MetaData,Table
from sqlalchemy.exc import OperationalError
from datetime import datetime
from typing import List, Dict, Tuple
from datetime import datetime, timedelta
import logging


Base.metadata.create_all(bind=engine)

# logging.basicConfig()
# logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

class Database():
    def __init__(self) -> None:
        super().__init__()

    def synchronize_model_with_database():
        lista = []
        inspector = inspect(engine)  # Inspeciona o banco de dados

        for table in Base.metadata.tables.values():
            table_name = table.name

            # Verifica se a tabela existe no banco de dados
            if table_name not in inspector.get_table_names():
                print(f"Creating missing table: {table_name}")
                table.create(engine)
                continue

            # Verifica colunas existentes na tabela
            existing_columns = {col['name'] for col in inspector.get_columns(table_name)}
            for column in table.columns:
                if column.name not in existing_columns:
                    try:
                        # Construir o comando ALTER TABLE manualmente
                        column_type = str(column.type)
                        default_value = f"DEFAULT {column.default.arg}" if column.default else ""
                        nullable = "NOT NULL" if not column.nullable else ""

                        alter_statement = f"""
                            ALTER TABLE {table_name}
                            ADD COLUMN {column.name} {column_type} {default_value} {nullable}
                        """.strip()

                        # Executa o comando
                        session.execute(text(alter_statement))
                        lista.append(f"column: {column.name} to table: {table_name}")
                    except OperationalError as e:
                        lista.append(f"Failed to add column {column.name}: {e}")
        return lista                


    def atualiza_schemas_bd(query):
        try : 
            sql_expression = text(query)
            query_execute =     session.execute(sql_expression)
            session.commit()

            for i in query_execute.fetchall():
                print(i)

            return True, "Atualizado"
    
        except  ValueError as e: 
            return False ,e


    def insert_table_cad_aplicativo(nome:str, obs:str,type:str = None, id: int = 0):
        match type:
            case None:
                try: 
                    new_cad =  CadastroApp(
                        nome=nome,
                        obs = obs
                    )

                    session.add(new_cad)            
                    session.commit()

                    return(True,new_cad.id)
                
                except ValueError as e:
                    session.rollback()
                    return(False,str(e))

            case 'update':
                try:
                    app = session.query(CadastroApp).filter(CadastroApp.id == id).first()

                    if app is None:
                        return (False, "App não encontrado.")
                    
                    app.nome = nome
                    app.obs = obs
                
                    session.add(app)            
                    session.commit()

                    return(True,app.id)
                
                except ValueError as e:
                    session.rollback()
                    return(False,str(e))
        
    def get_table_cad_aplicativo(type = None, id :int = None):

        lista = []
        match type:
            case "id":
                query = session.query(CadastroApp).filter_by(id=id)
                for i in query:
                    lista.append([i.id,i.nome,i.obs])
                return lista    
            case "list_id":
                query = session.query(CadastroApp)
                for i in query:
                    lista.append(i.id)
                return lista  
            
            case _:
                query = session.query(CadastroApp)
                for i in query:
                    lista.append([i.id,i.nome,i.obs])
                return lista  

    def delete_table_cad_aplicativo(id =  None):
        if isinstance(id, int):
            try:
                obj = session.query(CadastroApp).filter_by(id=id).first()  # Obter a primeira instância
                if obj:
                    session.delete(obj)  # Deletar a instância encontrada
                    session.commit()
                    return True
                else:
                    return False, "Nenhum valor encontrado"
            except ValueError as e:
                print(e)
                return False, e

    # @staticmethod
    # def add_data_bd_diario(data: List[Dict]):
    #     # Inicializa um dicionário para armazenar os dados processados que serão inseridos
    #     lanc_data = {}

    #     for item in data:
    #         campo = item['campo']
    #         valor = item['valor_entrada']
    #         tipo = item['tipo']
            
    #         # Ignorar campos vazios
    #         if valor == '':
    #             continue

    #         # Processamento e conversão dos tipos de dados conforme necessário
    #         if campo in ['km_lt', 'km_inicial', 'km_final', 'km_total','vlr_recebido','qt_total']:
    #             # Converte para float
    #             try:
    #                 lanc_data[campo] = float(valor)
    #             except ValueError:
    #                 print(f"Valor inválido para o campo '{campo}': {valor}")
    #                 continue  # Pular a inserção desse campo em caso de erro

    #         elif campo in ['qt_entregas']:
    #             # Converte para integer
    #             try:
    #                 lanc_data[campo] = int(valor)
    #             except ValueError:
    #                 print(f"Valor inválido para o campo '{campo}': {valor}")
    #                 continue

    #         elif campo in ['data_lanc']:
    #             # Converte para Date
    #             try:
    #                 lanc_data[campo] = datetime.strptime(valor, "%d/%m/%Y").date()#.strftime("%Y-%m-%d")
    #             except ValueError:
    #                 print(f"Data inválida para o campo '{campo}': {valor}")
    #                 continue

    #         elif campo in ['hora_inicial', 'hora_final','qt_hora' ]:
    #             # Converte para Time
    #             try:
    #                 lanc_data[campo] = datetime.strptime(valor, '%H:%M').time()
    #             except ValueError:
    #                 print(f"Hora inválida para o campo '{campo}': {valor}")
    #                 continue

    #         else:
    #             # Campos de texto ou strings diretas
    #             lanc_data[campo] = valor
 
    #     # Criar uma nova instância de LancEntrega com os dados processados
    #     try :
    #         novo_lanc = LancEntrega(**lanc_data)
        

    #         # Adiciona e faz commit da nova entrada ao banco de dados
    #         session.add(novo_lanc)
    #         session.commit()
    #         return(True,novo_lanc.id)
    #     except ValueError as e: 
    #         return(False, e)
        
    def get_next_cod_detalha(self,entrega_lanc):
        max_cod_detalha = session.query(func.max(LancEntregaItens.cod_detalha)).filter_by(entrega_lanc=entrega_lanc).scalar()
        return (max_cod_detalha or 0) + 1

    @staticmethod
    def add_data_bd_diario(data: List[Dict], **kwargs) -> Tuple[bool, int]:
        lanc_data = {}
        if "id" in kwargs:
            record_id = kwargs["id"]   # ID opcional para verificar se é atualização ou inserção
        else :
            record_id = 0    

        for item in data:
            campo = item['campo']
            valor = item['valor_entrada']
            
            if valor == '':
                continue  # Ignora campos vazios
            
            # Converte o valor conforme o tipo do campo
            if campo in ['km_lt', 'km_inicial', 'km_final', 'km_total', 'vlr_recebido', 'qt_total']:
                try:
                    lanc_data[campo] = float(valor)
                except ValueError:
                    print(f"Valor inválido para o campo '{campo}': {valor}")
                    continue
            elif campo == 'qt_entregas':
                try:
                    lanc_data[campo] = int(valor)
                except ValueError:
                    print(f"Valor inválido para o campo '{campo}': {valor}")
                    continue
            elif campo == 'data_lanc':
                try:
                    lanc_data[campo] = datetime.strptime(valor, "%d/%m/%Y").date()
                except ValueError:
                    print(f"Data inválida para o campo '{campo}': {valor}")
                    continue
            elif campo in ['hora_inicial', 'hora_final', 'qt_hora']:
                try:
                    lanc_data[campo] = datetime.strptime(valor, '%H:%M').time()
                except ValueError:
                    print(f"Hora inválida para o campo '{campo}': {valor}")
                    continue
            else:
                lanc_data[campo] = valor

        # Verifica se há um ID presente para decidir entre update ou insert
               
        
        try:
            if record_id > 0:
                # Verifica se o registro já existe no banco de dados
                registro_existente = session.query(LancEntrega).filter_by(id=record_id).first()
                if registro_existente:
                    # Atualiza os campos existentes
                    for campo, valor in lanc_data.items():
                        setattr(registro_existente, campo, valor)
                    session.commit()
                    return True, registro_existente.id
            else:
                # Cria um novo registro se o ID não foi fornecido
                novo_lanc = LancEntrega(**lanc_data)
                session.add(novo_lanc)
                session.commit()
                return True, novo_lanc.id
        except Exception as e:
            session.rollback()
            print(f"Erro ao inserir ou atualizar dados: {e}")
            return False, str(e)


    @staticmethod
    def delete_entrega_diario(id :int = 0, **kwargs):
        if isinstance(id, int):
            try:
                obj = session.query(LancEntrega).filter_by(id=id).first()  # Obter a primeira instância
                if obj:
                    session.delete(obj)  # Deletar a instância encontrada
                    session.commit()
                    return True
                else:
                    return False, "Nenhum valor encontrado"
            except ValueError as e:
                return False, e

    @staticmethod
    def add_data_detalhamento(tipo:str = 'insert',id_diario:int=0,**kwargs):
        if id_diario == 0:
            return False, "não é possivel add ou alterar sem o id do diario"
        
        if tipo == 'insert':
            try:
                for i in kwargs['data']:
                    max_cod_detalha  = session.query(func.max(LancEntregaItens.cod_detalha)).filter_by(entrega_lanc=id_diario).scalar()
                    max_cod_detalha = int(max_cod_detalha or 0) + 1
                    new =  LancEntregaItens(
                        cod_detalha = int(max_cod_detalha) ,
                        entrega_lanc = id_diario,
                        hora_inicial = datetime.strptime(i[1],"%H:%M").time(),
                        hora_final = datetime.strptime(i[2],"%H:%M").time(),
                        qt_hora = datetime.strptime(i[3],"%H:%M").time() if i[3] != "" else datetime.strptime("00:00","%H:%M").time(),
                        km_inicial=float(i[4]) if i[4] !='' else 0.0,
                        km_final = float(i[5]) if i[5] !='' else 0.0,
                        km_total = float(i[6]) if i[6] !='' else 0.0,
                        vlr_recebido = float(i[7]) if i[7] !='' else 0.0,
                        tp_pagamento = int(i[9]),
                        obs =  str(i[8])                       
                    )
                    session.add(new)
                    session.commit()
                # return True, new.id
            
            except Exception as e:
                session.rollback()
                
                return False, str(e)    

                
        elif tipo == 'update':
            try:
                for i in kwargs['data']:
                    update_deta = session.query(LancEntregaItens).filter(LancEntregaItens.cod_detalha == i[0],
                                                                         LancEntregaItens.entrega_lanc == id_diario
                                                                        ).first()
                    # update_deta.id = i[0]
                    # update_deta.cod_detalha = i[0]
                    update_deta.hora_inicial = datetime.strptime(i[1],"%H:%M").time()
                    update_deta.hora_final = datetime.strptime(i[2],"%H:%M").time()
                    update_deta.qt_hora = datetime.strptime(i[3],"%H:%M").time()
                    update_deta.km_inicial=float(i[4])
                    update_deta.km_final = float(i[5])
                    update_deta.km_total = float(i[6])
                    update_deta.vlr_recebido = float(i[7])
                    update_deta.obs =  str(i[8])
                    update_deta.tp_pagamento = int(i[9])

                    session.commit()
                # return True, update_deta.id 
            except Exception as e:
                session.rollback()
                print(f"Erro ao atualizar  dados: {e}")
                return False, str(e)    

    @staticmethod
    def delete_table_detalhamento(id:int = 0, cod_detalhe :int=0, entre_lanc:int = 0, **kwargs):
        if isinstance(cod_detalhe, int):
            try:
                obj = session.query(LancEntregaItens).filter(LancEntregaItens.cod_detalha == cod_detalhe,
                                                                         LancEntregaItens.entrega_lanc == entre_lanc
                                                                        ).first() 
                if obj :
                    session.delete(obj)
                    session.commit()
                    return True
            except ValueError as e: 
                return False, str(e)

        pass

    # @staticmethod
    # def get_table_lanc_diario(filter:bool = False, tipo:str ='', *args, **kwargs ):
        
    #     lista =[]
    #     if filter == True:
    #         match tipo:
    #             case 'id':
    #                 query = session.query(LancEntrega).filter_by(id=kwargs['valor']).all()
    #                 for i in query:
    #                     lista.append([i.id,i.app,i.data_lanc,i.hora_inicial,i.hora_final,i.qt_hora,i.km_lt,i.qt_entregas,i.vlr_recebido,i.obs,i.km_inicial,i.km_final,i.km_total])
    #                 pass
    #             case _: 
    #                 pass
    #         return lista    
    #     else:
    #         query = session.query(LancEntrega).all()
    #         for i in query:
    #             lista.append([i.id,i.app,i.data_lanc,i.hora_inicial,i.hora_final,i.qt_hora,i.km_lt,i.qt_entregas,i.vlr_recebido,i.obs])
                

                
    #         return lista

    #     pass   



    @staticmethod
    def get_table_lanc_diario(filter: bool = False, tipo: str = '', *args, **kwargs):
        """
        Obtém informações da tabela LancEntrega com base em filtros específicos.

        Args:
            filter (bool, optional): Indica se um filtro será aplicado. Defaults to False.
            tipo (str, optional): Tipo do filtro a ser utilizado ('id', 'data'). Defaults to ''.
            kwargs:
                - valor (var): Valor utilizado no filtro.
                - index_totalizado (int): 0 para Diário, 1 para Semanal, 2 para Mensal.

        Returns:
            list: Lista de resultados com as informações filtradas.
        """
        lista = []

        if filter:
            match tipo:
                case 'id':
                    query = session.query(LancEntrega).filter_by(id=kwargs['valor']).all()
                    for i in query:
                        lista.append([i.id, i.app, i.data_lanc, i.hora_inicial, i.hora_final, i.qt_hora, 
                                    i.km_lt, i.qt_entregas, i.vlr_recebido, i.obs, 
                                    i.km_inicial, i.km_final, i.km_total])

                case 'data':
                    if 'index_totalizado' in kwargs:
                        now = datetime.now().date()  # Data atual sem o horário
                        match kwargs['index_totalizado']:
                            case 1:  # Diário (hoje)
                                query = session.query(LancEntrega).filter(LancEntrega.data_lanc == now).all()
                                # for i in query:
                                #     lista.append([i.id, i.app, i.data_lanc, i.hora_inicial, i.hora_final, i.qt_hora, 
                                #                 i.km_lt, i.qt_entregas, i.vlr_recebido, i.obs, 
                                #                 i.km_inicial, i.km_final, i.km_total])
                            case 2:  # Semanal (últimos 7 dias)
                                start_date = now - timedelta(days=7)
                                query = session.query(LancEntrega).filter(
                                    LancEntrega.data_lanc.between(start_date, now)
                                ).all()
                                # for i in query:
                                #     lista.append([i.id, i.app, i.data_lanc, i.hora_inicial, i.hora_final, i.qt_hora, 
                                #                 i.km_lt, i.qt_entregas, i.vlr_recebido, i.obs, 
                                #                 i.km_inicial, i.km_final, i.km_total])
                            case 3:  # Mensal (últimos 30 dias)
                                start_date = now - timedelta(days=30)
                                query = session.query(LancEntrega).filter(
                                    LancEntrega.data_lanc.between(start_date, now)
                                ).all()
                                # for i in query:
                                #     lista.append([i.id, i.app, i.data_lanc, i.hora_inicial, i.hora_final, i.qt_hora, 
                                #                 i.km_lt, i.qt_entregas, i.vlr_recebido, i.obs, 
                                #                 i.km_inicial, i.km_final, i.km_total])

                            case _:  # Caso índice não seja reconhecido
                                query = []
                                
                    else:
                        query = []

                    for i in query:
                        lista.append([i.id, i.app, i.data_lanc, i.hora_inicial, i.hora_final, i.qt_hora, 
                            i.km_lt, i.qt_entregas, i.vlr_recebido, i.obs])

                case _:  # Tipo de filtro não reconhecido
                    pass

            return lista
        else:
            # Sem filtro, retorna todos os registros
            query = session.query(LancEntrega).all()
            for i in query:
                lista.append([i.id, i.app, i.data_lanc, i.hora_inicial, i.hora_final, i.qt_hora, 
                            i.km_lt, i.qt_entregas, i.vlr_recebido, i.obs])

            return lista



    @staticmethod
    def get_table_lanc_detalhamento(filter:bool = True, tipo:str = 'id', **kwargs):
        lista =[]
        if filter == True:
            match tipo:
                case 'id':
                    if "valor_cod_detalhe" in kwargs:
                        query = session.query(LancEntregaItens).filter(LancEntregaItens.cod_detalha == kwargs['valor_cod_detalhe'],
                                                                         LancEntregaItens.entrega_lanc == kwargs['valor']
                                                                        ).all()
                        for i in query:
                            lista.append([i.cod_detalha,i.hora_inicial,i.hora_final,i.qt_hora,i.km_inicial,i.km_final, i.km_total, i.vlr_recebido, i.obs, i.tp_pagamento])

                    else :
                        query = session.query(LancEntregaItens).filter_by(entrega_lanc=kwargs['valor']).all()
                        for i in query:
                            lista.append([i.cod_detalha,i.hora_inicial,i.hora_final,i.qt_hora,i.km_inicial,i.km_final, i.km_total, i.vlr_recebido, i.obs,i.tp_pagamento])


                    
                case _: 
                    pass
            return lista    
        else:
            query = session.query(LancEntrega).all()
            for i in query:
                lista.append([i.cod_detalha,i.hora_inicial,i.hora_final,i.qt_hora,i.km_inicial,i.km_final, i.km_total, i.vlr_recebido, i.obs,i.tp_pagamento])
                

                
            return lista

        pass  
        pass


    @staticmethod
    def insert_table_lanc_abastecimento(tipo:str = 'insert', id_lanc:int=0, **kwargs):
        if 'data_lanc' in kwargs:
            try:
                data_lanc_str = kwargs['data_lanc']
                data_lanc = datetime.strptime(data_lanc_str, "%d/%m/%Y %H:%M")
            except :
                data_lanc = kwargs['data_lanc']

        match tipo:
            case 'insert':
                try: 
                    new_lanc = LancAbastecimento(
                    data_lanc = data_lanc if 'data_lanc' in kwargs else None,
                    tp_combustivel = kwargs['tp_combustivel'] if 'tp_combustivel' in kwargs else None,
                    tp_pagamento = kwargs['tp_pagamento'] if 'tp_pagamento' in kwargs else None,
                    km_rodados = float(kwargs['km_rodados']) if 'km_rodados' in kwargs else 0.0, 
                    trip = float(kwargs['trip']) if 'trip' in kwargs else 0.0,
                    media_lt = float(kwargs['media_lt']) if 'media_lt' in kwargs else 0.0,
                    nome_posto = str(kwargs['nome_posto']) if 'nome_posto' in kwargs else None,
                    vlr_lt = float(kwargs['vlr_lt']) if 'vlr_lt' in kwargs else 0.0,
                    qt_abastecido =  float(kwargs['qt_abastecido']) if 'qt_abastecido' in kwargs else 0.0,
                    vlr_total =  float(kwargs['vlr_total']) if 'vlr_total' in kwargs else 0.0,
                    obs =  str(kwargs['obs']) if 'obs' in kwargs else ''
                    ) 
                    
                    session.add(new_lanc)
                    session.commit()

                    return True, new_lanc.id
                except ValueError as e: 
                    return False, e
                
            case 'update':
                try:

                    update_lanc = session.query(LancAbastecimento).filter(LancAbastecimento.id == kwargs['id']).first()
                    update_lanc.data_lanc = data_lanc if 'data_lanc' in kwargs else None
                    update_lanc.tp_combustivel = kwargs['tp_combustivel'] if 'tp_combustivel' in kwargs else None
                    update_lanc.tp_pagamento = kwargs['tp_pagamento'] if 'tp_pagamento' in kwargs else None
                    update_lanc.km_rodados = float(kwargs['km_rodados']) if 'km_rodados' in kwargs else 0.0 
                    update_lanc.trip = float(kwargs['trip']) if 'trip' in kwargs else 0.0
                    update_lanc.media_lt = float(kwargs['media_lt']) if 'media_lt' in kwargs else 0.0
                    update_lanc.nome_posto = str(kwargs['nome_posto']) if 'nome_posto' in kwargs else None
                    update_lanc.vlr_lt = float(kwargs['vlr_lt']) if 'vlr_lt' in kwargs else 0.0
                    update_lanc.qt_abastecido =  float(kwargs['qt_abastecido']) if 'qt_abastecido' in kwargs else 0.0
                    update_lanc.vlr_total =  float(kwargs['vlr_total']) if 'vlr_total' in kwargs else 0.0
                    update_lanc.obs =  str(kwargs['obs']) if 'obs' in kwargs else ''
                    
                    session.add(update_lanc)
                    session.commit()

                    return True, update_lanc.id
                except ValueError as e: 
                    return False, e

        # data_lanc =  Column(Date)
        # tp_combustivel =  Column(String)
        # tp_pagamento =  Column(String)
        # km_rodados = Column(Float)
        # trip = Column(Float)
        # media_lt = Column(Float)
        # nome_posto = Column(String)
        # vlr_lt = Column(Float, comment="Valor pago por litro")
        # qt_abastecido =  Column(Float, comment="Quantidade de litros Abastecidos")
        # vlr_total =  Column(Float, comment="Valor total pago pelo abastecimento")
        # obs =  Column(String)
        pass    
    
    @staticmethod
    def get_table_lanc_abastecimento(filter: bool = False, *args, **kwargs):
        lista = []
        match filter:
            case True:
                match kwargs['type_filter']:
                    case "id":
                        try: 
                            query =  session.query(LancAbastecimento).filter_by(id=kwargs['value_filter']).all()
                            for i in query:
                                lista.append([i.id,i.data_lanc,i.tp_combustivel,i.tp_pagamento,i.km_rodados,i.trip,i.media_lt,i.nome_posto,i.vlr_lt,i.qt_abastecido,i.vlr_total,i.obs])
                        except Exception as e:
                            return e
                    case "nome_posto":
                        try:
                            query =  session.query(LancAbastecimento).filter_by(nome_posto=kwargs['value_filter']).all()
                            for i in query:
                                lista.append([i.id,i.data_lanc,i.tp_combustivel,i.tp_pagamento,i.km_rodados,i.trip,i.media_lt,i.nome_posto,i.vlr_lt,i.qt_abastecido,i.vlr_total,i.obs])
                        except Exception as e:
                            return e
                    case "list_id":
                        try:
                            query =  session.query(LancAbastecimento)
                            for i in query:
                                lista.append(i.id)
                        except Exception as e:
                            return e
                pass
            case False: 
                try: 
                    query = session.query(LancAbastecimento).all()
                    for i in query:
                        lista.append([i.id,i.data_lanc,i.tp_combustivel,i.tp_pagamento,i.km_rodados,i.trip,i.media_lt,i.nome_posto,i.vlr_lt,i.qt_abastecido,i.vlr_total,i.obs])

                except ValueError as e: 
                    return e
        return lista            

    @staticmethod
    def delete_table_lan_abastecimento(id:int=0):
        if id !=0: 
            if isinstance(id, int):
                try:
                    obj = session.query(LancAbastecimento).filter_by(id=id).first()  # Obter a primeira instância
                    if obj:
                        session.delete(obj)  # Deletar a instância encontrada
                        session.commit()
                        return True,"Foi"
                    else:
                        return False, "Nenhum valor encontrado"
                except ValueError as e:

                    return False, e



if __name__=='__main__':
    app = Database.synchronize_model_with_database()#,type_filter='id', value_filter =5 , valor_cod_detalhe=4)
    print(app)