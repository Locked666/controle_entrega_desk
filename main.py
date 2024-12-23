import sys
import os
import qdarktheme
from PySide6 import QtCore
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt,QCoreApplication,QFile,Slot,SLOT,Signal,QRect,QObject, QTime,QAbstractTableModel,QDateTime
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget,QDialog,QVBoxLayout,QWidgetAction,QMdiSubWindow,QMessageBox,QCheckBox,QHeaderView,QMenu
import time
from time import sleep
from pathlib import Path

from datetime import datetime,date, time
from src.ui.Cadapp import Ui_CadApp
from src.ui.MainWindow import Ui_MainWindow
from src.ui.LancAbastecimento import Ui_LancAbastecimento
from src.ui.DisplaySearch import Ui_DisplaySearch
from src.ui.SelectThema import Ui_SelectThema
from src.ui.BootingSystem import Ui_booting_system
from database import Database
from ConfigApp import MODE_DEBUG, complement_ini, __version__,SELECT_THEMA_INI, PATH_DATABASE
from display_field_associed import DisplayAssociateTable


class Worket(QtCore.QObject):
    cadastro_app = Signal()
    save_data =  Signal()
    display_search_id_lanc_abastecimento =  Signal(int)
    display_search_id_cad_app =  Signal(int)
    toggle_thema_select = Signal(str)
    atualiza_viewer_display = Signal()

    ### initit ###

    # value_progressbar_booting = Signal(int)


class LoadingSystem(QtCore.QThread):
    value_progressbar_booting = QtCore.Signal(list)
    process_finish = QtCore.Signal()

    def __init__(self, worket: Worket):
        super().__init__()
        self.worket = worket
        self.path_script = os.path.join(Path(PATH_DATABASE).parent,'scripts')
        self.path_rel = os.path.join(Path(__file__).parent,'Relatorios')
        self.script_sql = []



    @Slot()
    def run(self, event=None):
        # print(self.path_script)
        # for i in range(10):
        #     self.value_progressbar_booting.emit([f'teste {i}',i])
        #     sleep(2)
        # calc =  self.__calc_progress()
        execute  = Database.synchronize_model_with_database()
        v = len(execute)
        if v == 0 or  v== "" :
            for i in range(10):
                percent = int(((i + 1) / 10) * 100)    
                self.value_progressbar_booting.emit([f'Verificando...',percent])
                sleep(0.2)  
                
            self.process_finish.emit()  
             
           

        # percent = int(((step + 1) / v) * 100)
        else : 
            for step,i in enumerate(execute):
                percent = int(((step + 1) / v) * 100)    
                self.value_progressbar_booting.emit([f'{i}',percent])
                sleep(0.4)
                
                # else : 
                #     self.value_progressbar_booting.emit([f'Atualizando Schemas',i])
            self.process_finish.emit()


    @Slot()
    def __very_script(self,event=None):

        pass

    @Slot()
    def __very_dependence(self,event=None):
        pass

    
    @Slot()
    def __calc_progress(self, event=None):
        contagem = 0
        self.value_progressbar_booting.emit([f'Calculando progresso ...',0])

        lista = self.__list_files()

       



        pass
    
    @Slot()
    def __list_files(self):
        if not os.path.exists(self.path_script):
            os.mkdir(self.path_script)

        if not os.path.exists(self.path_rel):
            os.mkdir(self.path_rel)    
            
        lista_files =  os.listdir(self.path_script)
        for i in lista_files:
            if i.endswith('.sql'):
                self.script_sql.append(i)

        return True 

        pass    

    @Slot()
    def __open_system(self,event=None):    
        app_main =  MainWindow(user="Admin", worket=self.worket)
        
        app_main.setStyleSheet(qdarktheme.load_stylesheet(SELECT_THEMA_INI))
        app_main.show()


class BootingSystem(QMainWindow, Ui_booting_system):
    def __init__(self, worket: Worket) -> None:
        super(BootingSystem, self).__init__() 
        self.worket = worket
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.loading = LoadingSystem(worket=self.worket)
        self.loading.value_progressbar_booting.connect(self.__update_progressbar)
        self.loading.process_finish.connect(self.__end_process)
        self.loading.start()

    @Slot()
    @Slot(int)
    def __update_progressbar(self, value):
        self.progressBar.setValue(int(value[1]))
        self.label_loading_execu.setText(str(value[0]))
        # if value[1] == 100:
        #     self.close()



    @Slot()
    def __start_process(self, event=None):
        
        # loading

        pass     
    
    

    @Slot()
    def __end_process(self,event=None):
        self.loading.terminate()
        self.close()
        Main = MainWindow(user='admin',worket=Worket())
        app.setStyleSheet(qdarktheme.load_stylesheet(SELECT_THEMA_INI))
        Main.show()

        pass

class SelectThema(QDialog, Ui_SelectThema):
    def __init__(self, worket: Worket) -> None:
        super().__init__(parent=None)
        self.setupUi(self)
        self.setWindowTitle(f"Seletor de Themas Controle de Entregas {__version__}")

        self.worket = worket

        self.bnt_okay.clicked.connect(self.callback_okay)

    @Slot()
    def callback_okay(self, event=None):

        if self.combobox_thema.currentText().strip() == 'Escuro':
            self.worket.toggle_thema_select.emit('dark')
        else :
            self.worket.toggle_thema_select.emit('light')

class TableModelSearch(QAbstractTableModel):
    def __init__(self, data,headers:list):
        super().__init__()
        self._data = data
        self._headers = headers
        if len(self._data) == 0:
            self.exit()

    def rowCount(self, parent=None):
        try:
            return len(self._data)
        except:
            return 0 
            pass

    def columnCount(self, parent=None):
        try:
            return len(self._data[0])
        except:
            return 0
            pass
        

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, date):
                return value.strftime('%d/%m/%Y')
            elif isinstance(value, time):
                return value.strftime('%H:%M')
            elif isinstance(value, datetime):
                pass
              #  print(value)
            return value
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        headers = self._headers
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                if 0 <= section < len(headers):
                    return headers[section]
                else:
                    return None
        return None
    
    def sort(self, column, order):
        self.layoutAboutToBeChanged.emit()
        self._data.sort(key=lambda x: x[column], reverse=(order == Qt.SortOrder.DescendingOrder))
        self.layoutChanged.emit()

    def add_row(self, new_data):
        """
        Adiciona uma nova linha ao modelo e notifica a tabela.
        """
        self.beginInsertRows(self.index(len(self._data), 0).parent(), len(self._data), len(self._data))
        self._data.append(new_data)
        self.endInsertRows()

    def remove_rows(self, rows):
        """
        Remove as linhas especificadas pela lista de índices 'rows'.
        """
        rows = sorted(rows, reverse=True)  # Ordena de forma decrescente para evitar problemas de índice
        for row in rows:
            if 0 <= row < len(self._data):
                self.beginRemoveRows(self.index(row, 0).parent(), row, row)
                del self._data[row]
                self.endRemoveRows()   

    def clear(self):
        """
        Remove todos os dados da tabela.
        """
        self.beginRemoveRows(self.index(0, 0).parent(), 0, len(self._data) - 1)
        self._data.clear()
        self.endRemoveRows()                 

    def exit(self):
        return

class DisplaySearch(QDialog,Ui_DisplaySearch ):
    def __init__(self, worket: Worket, data, title, headers,v_signal) -> None:
        super().__init__(parent=None)
        self.worket = worket
        self._title = title
        self._data = data
        self._headers = headers
        self._v_signal = v_signal
        
        
        try:
            self.setupUi(self)
        except Exception as e:

            reply = QMessageBox.question(self, 'Confirmar Saída',
                                     f'Erro ao inicializar LancAbastecimento: {e}',
                                     QMessageBox.Yes)
        
        self.label_2.setText(str(len(data)))
        self.setWindowTitle(f"Pesquisa {self._title}  - Controle de Entregas{__version__}")

        
        
        self.bnt_select.clicked.connect(self.callback_bnt_select)
        self.bnt_cancelar.clicked.connect(self.callback_bnt_cancelar)
        self.table_search_content.doubleClicked.connect(self.callback_bnt_select)
        self.combo_column_search.addItems(self._headers)
        self.model_search = TableModelSearch(data=data,headers=self._headers)
       
        self.table_search_content.setModel(self.model_search)
        self.table_search_content.setSortingEnabled(True)
        self.table_search_content.horizontalHeader().sectionClicked.connect(self.sort_table)
        self.bnt_search.clicked.connect(self.filter_table)

    @Slot()
    def filter_table(self):
        selected_column = self.combo_column_search.currentIndex()
        search_term = self.text_content_search.text().lower()
        if search_term == "": 
            self.model_search._data = self._data
            self.model_search.layoutChanged.emit() 
            return
        
        if "data" in self.combo_column_search.currentText().lower():
            try:
                # Converte o termo de pesquisa para um objeto datetime
                search_date = datetime.strptime(search_term, "%d/%m/%Y").date()
                search_date = search_date.strftime("%Y-%m-%d")
                search_date = datetime.strptime(search_date, "%Y-%m-%d").date()

                # Filtra os dados com base na data
                # filtered_data = [row for row in self.model_search._data if search_date == row[selected_column].date()]
                
                filtered_data = [row for row in self._data if search_date == row[selected_column].date()]
 
                self.model_search._data = filtered_data
                self.model_search.layoutChanged.emit()
            except ValueError:
                reply = QMessageBox.warning(self, 'Formato Inválido',
                                     f"Formato de data inválido. Use o formato DD/MM/AAAA.",
                                     QMessageBox.Yes)


        
        else :
            filtered_data = [row for row in self._data if search_term in str(row[selected_column]).lower()]
            self.model_search._data = filtered_data
            self.model_search.layoutChanged.emit()    

    @Slot()
    def callback_click_table(self, index=None, event=None):
        row = index.row()
        row_data = [self.model_search.data(self.model_search.index(row, col), Qt.DisplayRole) for col in range(self.model_search.columnCount(None))]

    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.callback_bnt_select()
        else:
            super().keyPressEvent(event)

    @Slot()
    def sort_table(self, column):
        self.combo_column_search.setCurrentIndex(column)
        order = self.table_search_content.horizontalHeader().sortIndicatorOrder()
        self.table_search_content.sortByColumn(column, order)

    @Slot()
    def callback_bnt_cancelar(self):
        self.destroy()
        


    @Slot()
    def callback_bnt_select(self):
        selected_indexes = self.table_search_content.selectionModel().selectedRows()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            row_data = [self.model_search.data(self.model_search.index(selected_row, col), Qt.DisplayRole) for col in range(self.model_search.columnCount(None))]
            self._v_signal.emit(row_data[0])
            self.destroy()

        else:
           reply = QMessageBox.warning(self, 'Selecione uma linha',
                                     f'Nenhuma Linha selecionada!',
                                     QMessageBox.Yes)

class LancAbastecimento(QDialog, Ui_LancAbastecimento):
    def __init__(self, worket: Worket) -> None:
        super().__init__(parent=None)
        self.worket = worket
        
        try:
            self.setupUi(self)
        except Exception as e:

            reply = QMessageBox.question(self, 'Confirmar Saída',
                                     f'Erro ao inicializar LancAbastecimento: {e}',
                                     QMessageBox.Yes)

        self.setWindowTitle(f"Lançamento de Abastecimento - Controle de Entregas{__version__}")
        self.worket.display_search_id_lanc_abastecimento.connect(self.populate_field)
        self.bnt_adicionar.clicked.connect(self.callback_bnt_adicionar)
        self.bnt_alterar.clicked.connect(self.callback_bnt_alterar)
        self.bnt_cancelar.clicked.connect(self.callback_bnt_cancelar)
        self.bnt_salvar.clicked.connect(self.callback_bnt_salvar)
        self.bnt_excluir.clicked.connect(self.callback_bnt_excluir)
        self.bnt_search.clicked.connect(self.callback_bnt_search)
        self.bnt_next.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="next"))
        self.bnt_next_full.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="next_full"))
        self.bnt_back_full.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="back_full"))
        self.bnt_back.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="back"))
        self.__state_field('disabled')


    @Slot()
    def callback_bnt_seq_info(self, tipo):
        value_in_db =  Database.get_table_lanc_abastecimento(filter=True,type_filter='list_id')
        
        value_id = self.lcd_id.intValue()
        if len(value_in_db) == 0 :
            self.clear_field()
            self.lcd_id.setProperty(u'intValue', 0)
        self.lbl_total.setText(str(len(value_in_db)))
        

        match tipo:
            case "back":
                if value_id == 0:
                    return
                else:
                    if value_id == 0:
                        for i in value_in_db:
                            self.populate_field(id=i)
                            return
                    else:
                        if len(value_in_db) > 1: 

                            a = value_in_db.index(value_id)
                            a -= 1
                            try:
                                b = value_in_db[a]
                                self.populate_field(id=b)
                            except:
                                return   
            
            case "back_full":
                if value_id == 0:
                    return
                else:
                    self.populate_field(id=min(value_in_db))
            
            case "next":
                if value_id == 0:
                    for i in value_in_db:
                        self.populate_field(id=i)
                        return
                else:
                    if len(value_in_db) > 1: 

                        a = value_in_db.index(value_id)
                        a += 1
                        try:
                            b = value_in_db[a]
                            self.populate_field(id=b)
                        except:
                            return    


            case "next_full":
                if value_id == max(value_in_db):
                    return
                else:
                    self.populate_field(id=max(value_in_db))


        pass

    @Slot()
    def callback_bnt_adicionar(self):
        self.__control_button("edicao")
        self.__clear_field()
        self.__state_field('enabled')


    @Slot()
    def callback_bnt_search(self):
        dados =  Database.get_table_lanc_abastecimento()
        headers = ['Código', 'Data Lançamento', 'Tp Combustivel', 'tipo Pagamento', 'km Rodados' , 'trip', 'media LT','Nome do Posto' ,'Valor Litro', 'Qt Abastecido', 'Valor Total', 'Obs']
        display_search = DisplaySearch(self.worket,data=dados, title='Abastecimento', headers=headers, v_signal=self.worket.display_search_id_lanc_abastecimento).exec()
        pass


    @Slot()
    def callback_bnt_alterar (self):
        if self.lcd_id.intValue() == 0 :
            reply = QMessageBox.warning(self, 'Atenção !!',
                                     f'Nenhum Lançamento selecionado',
                                     QMessageBox.Yes) 
        else :
            self.__control_button("edicao")
            self.__state_field('enabled') 


    @Slot()
    def callback_bnt_cancelar(self):
        if self.bnt_alterar.isEnabled():
            self.destroy() 
            
        else :  
            reply = QMessageBox.question(self, 'Atenção',
                                     f'O Lançamento está em modo de edição, deseja cancelar a operação ?',
                                     QMessageBox.Yes | QMessageBox.No) 
            if reply == QMessageBox.Yes:
                if self.lcd_id.intValue() == 0: 
                    self.__clear_field()
                    self.__state_field("disabled")
                    self.__control_button("viewer")
                else :
                    self.__state_field("disabled")
                    self.__control_button("viewer")

    @Slot()
    def callback_bnt_salvar(self):
        data = self.__get_value_display()
        if self.lcd_id.intValue() == 0 :
          
            insert = Database.insert_table_lanc_abastecimento(
                data_lanc = QDateTime.toString(self.date_lanc_abastecimento.dateTime(),"dd/MM/yyyy HH:mm"),
                tp_combustivel =  data['combobox_tipo_combustivel'],
                tp_pagamento =  data['combobox_tipo_pagamento'],
                km_rodados =data['text_km_rodados'].replace(',','.').strip() if data['text_km_rodados'] != "" else 0.0,
                trip = data['text_trip'].replace(',','.').strip() if data['text_trip'] != "" else 0.0,
                media_lt = data['text_media_lt'].replace(',','.').strip() if data['text_media_lt'] != "" else 0.0 ,
                nome_posto = data['text_nome_posto'].replace(',','.').strip() if data['text_nome_posto'] != "" else "S/ Nome",
                vlr_lt = data['text_valor_lt'].replace(',','.').strip() if data['text_valor_lt'] != "" else 0.0,
                qt_abastecido =  data['text_qt_lt'].replace(',','.').strip() if data['text_qt_lt'] != "" else 0.0,
                vlr_total =  data['text_valor_total'].replace(',','.').strip() if data['text_valor_total'] != "" else 0.0,
                obs =  data['plain_obs'].strip(),
            )
            if insert[0] == True:
                reply = QMessageBox.information(self, 'Lançamento',
                                     f'Lançamento realizado com sucesso no código: {insert[1]} ',
                                     QMessageBox.Yes)
                
                self.lcd_id.setProperty("intValue",insert[1])
                self.__control_button("viewer")
                self.__state_field('disabled')

            else :
                reply = QMessageBox.warning(self, 'Warning',
                                     f'Ocorreu um erro ao efetuar o lançamento:\n {insert[1]} ',
                                     QMessageBox.Yes)     

        else :
            update = Database.insert_table_lanc_abastecimento(
                tipo='update',
                id = self.lcd_id.intValue(),
                data_lanc = QDateTime.toString(self.date_lanc_abastecimento.dateTime(),"dd/MM/yyyy HH:mm") ,#data['qt_spinbox_lineedit'],
                tp_combustivel =  data['combobox_tipo_combustivel'],
                tp_pagamento =  data['combobox_tipo_pagamento'],
                km_rodados =data['text_km_rodados'].replace(',','.').strip() if data['text_km_rodados'] != "" else 0.0,
                trip = data['text_trip'].replace(',','.').strip() if data['text_trip'] != "" else 0.0,
                media_lt = data['text_media_lt'].replace(',','.').strip() if data['text_media_lt'] != "" else 0.0 ,
                nome_posto = data['text_nome_posto'].replace(',','.').strip() if data['text_nome_posto'] != "" else "S/ Nome",
                vlr_lt = data['text_valor_lt'].replace(',','.').strip() if data['text_valor_lt'] != "" else 0.0,
                qt_abastecido =  data['text_qt_lt'].replace(',','.').strip() if data['text_qt_lt'] != "" else 0.0,
                vlr_total =  data['text_valor_total'].replace(',','.').strip() if data['text_valor_total'] != "" else 0.0,
                obs =  data['plain_obs'].strip(),
            )
            if update[0] == True:
                reply = QMessageBox.information(self, 'Lançamento',
                                     f'Lançamento realizado com sucesso no código: {update[1]} ',
                                     QMessageBox.Yes)
                
                self.__control_button("viewer")
                self.__state_field('disabled')

            else :
                reply = QMessageBox.warning(self, 'Warning',
                                     f'Ocorreu um erro ao efetuar o lançamento:\n {update[1]} ',
                                     QMessageBox.Yes)


    @Slot()
    def callback_bnt_excluir(self):
        
        if self.lcd_id.intValue()!= 0:
            reply = QMessageBox.question(self, 'Confirmar Exclusão',
                                     'Você realmente deseja excluir o lançamento?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes : 
                delete = Database.delete_table_lan_abastecimento(id= self.lcd_id.intValue())
                if delete[0]:
                    reply = QMessageBox.information(self, 'Exclusão do Lançamento',
                                        f'Foi realizado a Exclusão do Lançamento:{self.lcd_id.intValue()} ',
                                        QMessageBox.Yes)
                    self.__clear_field()
                else: 
                    reply = QMessageBox.warning(self, 'Exclusão do Lançamento',
                                        f'Ocorreu um erro ao efetuar a exclusão:\n {delete[1]} ',
                                        QMessageBox.Yes)
        else :
            reply = QMessageBox.warning(self, 'Exclusão do Lançamento',
                                    f'Nenhum Lançamento selecionado.',
                                    QMessageBox.Yes) 


    @Slot()
    @Slot(int)
    def populate_field(self,id:int=0):
        # [i.id,i.data_lanc,i.tp_combustivel,i.tp_pagamento,i.km_rodados,i.trip,i.media_lt,i.nome_posto,i.vlr_lt,i.qt_abastecido,i.vlr_total,i.obs]
        if id != 0: 
            value = Database.get_table_lanc_abastecimento(filter=True,type_filter='id', value_filter = id)
            value = value[0]
            self.lcd_id.setProperty(u"intValue",value[0])
            self.date_lanc_abastecimento.setDateTime(QDateTime(value[1]))
            self.combobox_tipo_combustivel.setCurrentText(value[2])
            self.combobox_tipo_pagamento.setCurrentText(value[3])
            self.text_km_rodados.setText(str(value[4]))
            self.text_trip.setText(str(value[5]))
            self.text_media_lt.setText(str(value[6]))
            self.text_nome_posto.setText(str(value[7]))
            self.text_valor_lt.setText(str(value[8]))
            self.text_qt_lt.setText(str(value[9]))
            self.text_valor_total.setText(str(value[10]))
            self.plain_obs.setPlainText(str(value[11]))


    @Slot()
    def __get_value_display(self):
        data = {}
        field = []
        for i in self.tabWidget_3.findChildren(QWidget):
            field.append(i)
            

        for i in field:
            if type(i).__name__ == 'QLineEdit': #or type(i).__name__ == 'QPlainTextEdit':
                data[f'{i.objectName()}'] = i.text()
            elif type(i).__name__ == 'QPlainTextEdit' :
                data[f'{i.objectName()}'] = i.toPlainText()

            elif type(i).__name__ == 'QTimeEdit':
                data[f'{i.objectName()}'] = i.dateTime()

            elif  type(i).__name__ == 'QComboBox': 
                data[f'{i.objectName()}'] = i.currentText()

            elif  type(i).__name__ == 'QLineEdit': 
                data[f'{i.objectName()}'] = i.intValue()

            # else: 
            #     data[f'{i.objectName()}'] = type(i).__name__
        return data

    @Slot()
    def __control_button(self,method):
        """_summary_

        Args:
            method (str): "edicao", "viewer":
        """
        match method.lower(): 
            case "edicao":
                ### Inativos
                self.bnt_alterar.setEnabled(False)
                self.bnt_adicionar.setEnabled(False)
                self.bnt_search.setEnabled(False)
                self.bnt_excluir.setEnabled(False)
                self.bnt_back.setEnabled(False)
                self.bnt_back_full.setEnabled(False)
                self.bnt_next.setEnabled(False)
                self.bnt_next_full.setEnabled(False)
                # Ativos 
                self.bnt_salvar.setEnabled(True)
                

            case "viewer":
                # Ativos 
                self.bnt_alterar.setEnabled(True)
                self.bnt_adicionar.setEnabled(True)
                self.bnt_search.setEnabled(True)
                self.bnt_excluir.setEnabled(True)
                self.bnt_back.setEnabled(True)
                self.bnt_back_full.setEnabled(True)
                self.bnt_next.setEnabled(True)
                self.bnt_next_full.setEnabled(True)
                ### Inativos
                self.bnt_salvar.setEnabled(False)      
        pass

    @Slot()
    def __clear_field(self):
        field = []
        self.lcd_id.setProperty(u"intValue",0)
        for i in self.tabWidget_3.findChildren(QWidget):
            field.append(i)

        for i in field:
            if type(i).__name__ == 'QLineEdit' or type(i).__name__ == 'QPlainTextEdit':
                i.clear() 
            elif type(i).__name__ == 'QTimeEdit':
                i.setTime(QTime(0, 0))       

    @Slot()
    def __state_field(self, state):
        match state.lower():
            case 'disabled':
                self.tabWidget_3.setTabEnabled(0,False)
            case 'enabled':
                self.tabWidget_3.setTabEnabled(0,True)    
            case _:
                raise "não identificado, seria disabled ou enabled"    

    @Slot()
    def closeEvent(self, event,t=None):

        reply = QMessageBox.question(self, 'Confirmar Saída',
                                     'Você realmente fechar o lançamento?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()  # Aceita o fechamento da janela
            self.destroy()

class CadastroAplicativos(QDialog,Ui_CadApp):
    def __init__(self, worket: Worket) -> None:
        super().__init__(parent=None)
        self.worket = worket
        
       
        
        self.setupUi(self)
        self.setWindowTitle(f"Cadastro de Aplicativos - Controle de Entregas{__version__}")
        self.worket.display_search_id_cad_app.connect(self.populate_field)
        self.bnt_alterar.clicked.connect( self.callback_bnt_alterar)
        self.bnt_cancelar.clicked.connect(self.callback_bnt_cancela)
        self.bnt_adicionar.clicked.connect(self.callback_bnt_incluir)
        self.bnt_search.clicked.connect(self.callback_bnt_search)
        self.bnt_excluir.clicked.connect(self.callback_bnt_delete)
        self.bnt_next.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="next"))
        self.bnt_next_full.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="next_full"))
        self.bnt_back_full.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="back_full"))
        self.bnt_back.clicked.connect(lambda: self.callback_bnt_seq_info(tipo="back"))
        self.bnt_salvar.clicked.connect(self.callback_bnt_save)
        # Permite menu de contexto
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        


        self.field_text = [self.text_nome, self.plain_obs]
        self.field_check = []

        self.verify_field()

    def get_value(self):
        value = []

        for i in self.field_text:
            if i.objectName() != 'plain_obs':
                a = {i.objectName():i.text()}
                # a = dict(i.objectName(),i.text())
            else:
                a = {i.objectName():i.toPlainText()}    
                # a = dict(i.objectName(),i.toPlainText())
            value.append(a)
        return value    



    

    def show_context_menu(self, position):
        # Criação do menu
        menu = QMenu(self)

        # Adicionando ações ao menu
        action_1 = menu.addAction("Opção 1")
        action_2 = menu.addAction("Opção 2")
        action_3 = menu.addAction("Sair")

        # Exibe o menu
        action = menu.exec_(self.mapToGlobal(position))

        # Tratamento das ações
        if action == action_1:
            QMessageBox.information(self, "Ação", "Você clicou em Opção 1!")
        elif action == action_2:
            QMessageBox.information(self, "Ação", "Você clicou em Opção 2!")
        elif action == action_3:
            self.close()

    @Slot()
    @Slot(int)
    def populate_field(self,id:int=None):
        if id == None:
            value = Database.get_table_cad_aplicativo()
        else :
            self.clear_field()
            value = Database.get_table_cad_aplicativo(type='id', id=id)
            value = value[0]
            if len(value) > 0: 
                self.lcd_id.setProperty(u"intValue",value[0])
                self.text_nome.setText(value[1])    
                self.plain_obs.insertPlainText(value[2])    

    def verify_field(self, read_text:bool = True, enabled_check:bool = False):

        for i in self.field_text:
            if i.isReadOnly() != read_text:
                i.setReadOnly(read_text)

        for e in self.field_check:
            if e.isEnabled() != enabled_check:
                e.setEnabled(enabled_check)

    def clear_field(self):
        for i in self.field_text:
            i.clear()
        pass

    def callback_bnt_alterar(self):
        
        label_id = self.lcd_id.value()
        if label_id != 0:
            self.verify_field(False,True)
            self.bnt_alterar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_search.setEnabled(False)
            self.bnt_excluir.setEnabled(False)
            self.modal_seq_info()
            
        else:
            reply = QMessageBox.question(self, 'Error',
                                     'Nenhuma empresa Selecionada',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.verify_field(True,False)

    def modal_seq_info(self, form:bool = False):
        self.bnt_back.setEnabled(form)
        self.bnt_back_full.setEnabled(form)
        self.bnt_next.setEnabled(form)
        self.bnt_next_full.setEnabled(form)
    

    def callback_bnt_incluir(self):
        if self.bnt_alterar.isEnabled() == True:
            self.clear_field()
            self.verify_field(False,True)
            self.lcd_id.setProperty(u"intValue", 0)
            self.bnt_alterar.setEnabled(False)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_search.setEnabled(False)
            self.bnt_excluir.setEnabled(False)
            self.modal_seq_info()

    def callback_bnt_cancela(self):
        label_id = self.lcd_id.value()
        if self.bnt_alterar.isEnabled():
            self.destroy()
        if label_id == 0:
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.clear_field()
            # self.populate_field()
            self.modal_seq_info(True)
        else:    
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.modal_seq_info(True)

    def callback_bnt_seq_info(self, tipo):
        value_in_db =  Database.get_table_cad_aplicativo(type='list_id')
        
        value_id = self.lcd_id.value()
        if len(value_in_db) == 0 :
            self.clear_field()
            self.lcd_id.setProperty(u'intValue', 0)
        self.lbl_total.setText(str(len(value_in_db)))
        

        match tipo:
            case "back":
                if value_id == 0:
                    return
                else:
                    if value_id == 0:
                        for i in value_in_db:
                            self.populate_field(id=i)
                            return
                    else:
                        if len(value_in_db) > 1: 

                            a = value_in_db.index(value_id)
                            a -= 1
                            try:
                                b = value_in_db[a]
                                self.populate_field(id=b)
                            except:
                                return   
            
            case "back_full":
                if value_id == 0:
                    return
                else:
                    self.populate_field(id=min(value_in_db))
            
            case "next":
                if value_id == 0:
                    for i in value_in_db:
                        self.populate_field(id=i)
                        return
                else:
                    if len(value_in_db) > 1: 

                        a = value_in_db.index(value_id)
                        a += 1
                        try:
                            b = value_in_db[a]
                            self.populate_field(id=b)
                        except:
                            return    


            case "next_full":
                if value_id == max(value_in_db):
                    return
                else:
                    self.populate_field(id=max(value_in_db))


        pass

    def callback_bnt_delete(self):
        value_id = self.lcd_id.intValue()
        d = Database.delete_table_cad_aplicativo(int(value_id))

        if d is True: 
            reply = QMessageBox.question(self, 'Foi',
                                     'aplicativo Excluido com sucesso',
                                     QMessageBox.Ok | QMessageBox.No)
            self.verify_field()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.modal_seq_info(True)
            self.worket.cadastro_app.emit()
            self.clear_field()
            self.lcd_id.setProperty(u'intValue',0)
            
        else : 
            reply = QMessageBox.question(self, 'Foi',
                                     f'Erro: {d}',
                                     QMessageBox.Ok | QMessageBox.No)

    def callback_bnt_save(self):
        if self.lcd_id.intValue() == 0:
            insert =  Database.insert_table_cad_aplicativo(
                nome =  self.text_nome.text().strip(),
                obs = self.plain_obs.toPlainText().strip()
            )
        else: 
            insert =  Database.insert_table_cad_aplicativo(
                type ='update',
                id = self.lcd_id.intValue(),
                nome =  self.text_nome.text().strip(),
                obs = self.plain_obs.toPlainText().strip()
            )    

        if insert[0]: 
            reply = QMessageBox.question(self, 'Foi',
                                     'aplicativo inserido com sucesso',
                                     QMessageBox.Ok | QMessageBox.No)
            self.verify_field()
            self.lcd_id.setProperty(u'intValue',insert[1])
            self.worket.cadastro_app.emit()
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.modal_seq_info(True)

    @Slot()
    def callback_bnt_search(self):
        dados =  Database.get_table_cad_aplicativo()
        headers =  ['Código', 'App', 'Observação']
        display_search = DisplaySearch(self.worket,data=dados, title='Abastecimento', headers=headers, v_signal=self.worket.display_search_id_cad_app).exec()
        pass

class TableModelDiario(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        if len(self._data) == 0:
            self.exit()

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        try:
            return len(self._data[0])
        except:
            return 0
            pass

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, date):
                return value.strftime('%d/%m/%Y')
            elif isinstance(value, time):
                return value.strftime('%H:%M')
            return value
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        headers = ["Código", "App", "Data", "Hora Inicial","Hora Final" ,"Qt Horas", "KM/Lt", "QT Entregas", "Valor Recebido", "OBS"]
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                if 0 <= section < len(headers):
                    return headers[section]
                else:
                    return None
        return None
    
    def clear(self):
        """
        Remove todos os dados da tabela.
        """
        self.beginRemoveRows(self.index(0, 0).parent(), 0, len(self._data) - 1)
        self._data.clear()
        self.endRemoveRows()

    def exit(self):
        return

class TableModelDetalhamento(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        if len(self._data) == 0:
            self.exit()

    def rowCount(self, parent=None):
        try:
            return len(self._data)
        except:
            return 0 
            pass

    def columnCount(self, parent=None):
        try:
            return len(self._data[0])
        except:
            return 0
            pass
        

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            value = self._data[index.row()][index.column()]
            if isinstance(value, date):
                return value.strftime('%d/%m/%Y')
            elif isinstance(value, time):
                return value.strftime('%H:%M')
            return value
        return None

    def headerData(self, section, orientation, role=Qt.ItemDataRole.DisplayRole):
        headers = ["Código","Hora Inicial", "Hora Final", "Qt Horas", "km Inicial", "KM Final", "Km Total", "Valor Recebido", "OBS", "Tipo Pagamento"]
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                if 0 <= section < len(headers):
                    return headers[section]
                else:
                    return None
        return None
    


    def add_row(self, new_data):
        """
        Adiciona uma nova linha ao modelo e notifica a tabela.
        """
        self.beginInsertRows(self.index(len(self._data), 0).parent(), len(self._data), len(self._data))
        self._data.append(new_data)
        self.endInsertRows()

    def remove_rows(self, rows):
        """
        Remove as linhas especificadas pela lista de índices 'rows'.
        """
        rows = sorted(rows, reverse=True)  # Ordena de forma decrescente para evitar problemas de índice
        for row in rows:
            if 0 <= row < len(self._data):
                self.beginRemoveRows(self.index(row, 0).parent(), row, row)
                del self._data[row]
                self.endRemoveRows()   

    def clear(self):
        """
        Remove todos os dados da tabela.
        """
        self.beginRemoveRows(self.index(0, 0).parent(), 0, len(self._data) - 1)
        self._data.clear()
        self.endRemoveRows()                 

    def exit(self):
        return

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,user,worket: Worket) -> None:
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle(f"Controle de Entregas {__version__}")
        self.user_logado = user
        self.row_table_detalhamento = ""
        self.worket = worket #Worket()
        self.worket.cadastro_app.connect(self.populate_check_box)
        self.worket.save_data.connect(self.populate_little_info_frame )
        self.worket.save_data.connect(self.populate_little_info_frame_detalhamento )
        self.worket.toggle_thema_select.connect(self.toggle_thema)
        self.worket.save_data.connect(lambda : self.populate_table_detalhemento(id_lanc=self.lcd_id.intValue()))
        self.tableView_2.horizontalHeader().sectionClicked.connect(self.sort_table)
        self.disable_tab_widgets()
        self.populate_little_info_frame()
        self.populate_table_detalhemento()
        self.populate_check_box()
       

        self.field_text = []
        self.field_check = []

        self.lanc_diario_time_hora_final.editingFinished.connect(lambda: self.on_calc_time(time_1=self.lanc_diario_time_hora_inicial, time_2=self.lanc_diario_time_hora_final,total=self.lanc_diario_text_qt_horas))
        self.lanc_entrega_time_hora_final_2.editingFinished.connect(lambda: self.on_calc_time(time_1=self.lanc_entrega_time_hora_inicial_2, time_2=self.lanc_entrega_time_hora_final_2,total=self.lanc_entrega_text_qt_horas_2))
        
        self.lanc_diario_text_km_final.editingFinished.connect(lambda: self.on_calc_km(text=self.lbl_error_diario, km_1=self.lanc_diario_text_km_inicial, km_2=self.lanc_diario_text_km_final,total=self.lanc_diario_text_km_total))
        self.lanc_entrega_text_km_final_2.editingFinished.connect(lambda: self.on_calc_km(text=self.lbl_error_entregas, km_1=self.lanc_entrega_text_km_inicial_3, km_2=self.lanc_entrega_text_km_final_2, total=self.lanc_entrega_text_km_total_3))
        self.combobox_set_totalizado.currentIndexChanged.connect(self.populate_little_info_frame)

        self.bnt_alterar.clicked.connect( self.callback_bnt_alterar)
        self.bnt_cancelar.clicked.connect(self.callback_bnt_cancela)
        self.bnt_adicionar.clicked.connect(self.callback_bnt_incluir)
        self.bnt_excluir.clicked.connect(self.callback_bnt_delete)
        self.bnt_salvar.clicked.connect(self.callback_bnt_salvar)
        self.lanc_entrega_bnt_add.clicked.connect(self.get_value_detalhamento)
        self.lanc_entrega_bnt_delete.clicked.connect(self.callback_bnt_delete_detalhamento)
        self.lanc_diario_tableView.clicked.connect(self.callback_click_row_table_diario)
        self.tableView_2.clicked.connect(self.callback_click_row_table_detalhamento)

        self.actionAplicativos.triggered.connect(lambda: CadastroAplicativos(self.worket).show())
        self.actionAbastecimento.triggered.connect(lambda: LancAbastecimento(self.worket).exec())
        self.actionTema.triggered.connect(lambda: SelectThema(self.worket).exec())

    @Slot(str)
    def toggle_thema(self,thema):
        # print(thema)
        complement_ini('Settings','thema',thema)
        app.setStyleSheet(qdarktheme.load_stylesheet(thema))
        


    @Slot()
    def sort_table(self, column):

        order = self.tableView_2.horizontalHeader().sortIndicatorOrder()
        self.tableView_2.sortByColumn(column, order)

    @Slot()
    def disable_tab_widgets(self,status:bool = True):
        self.frm_widget_info.setDisabled(status)
        self.frm_widger_entrega.setDisabled(status)
            
    @Slot() 
    def callback_bnt_salvar(self):
        value = self.get_value()
        if self.lcd_id.intValue() == 0:
            insert = Database.add_data_bd_diario(value )
        else :  
            insert = Database.add_data_bd_diario(value,id = self.lcd_id.intValue())   

        if insert[0]:
            self.disable_tab_widgets(True)
            self.lcd_id.setProperty(u"intValue", insert[1])
            self.lanc_diario_tableView.setEnabled(True)
            self.tableView_2.setEnabled(True)
            self.bnt_adicionar.setEnabled(True)
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_excluir.setEnabled(True)
            
            
            self.save_detalhamento(id_diario=insert[1])
            self.worket.save_data.emit()
            reply = QMessageBox.information(self, 'Viagem Salva ',
                                     f'A Viagem foi salva com sucesso\n Código: {insert[1]}',
                                     QMessageBox.Yes)
        else: 
              reply = QMessageBox.critical(self, 'Erro ao salvar viagem',
                                     f'Ocorreu um erro ao salvar informação\n Erro: {insert[1]}',
                                     QMessageBox.Yes)  

    def on_calc_time(self,time_1, time_2, total):
        # Definindo os horários
        hora_inicial = time_1.time()
        hora_final = time_2.time()

        # Convertendo ambos os tempos para segundos desde a meia-noite
        total_segundos_inicial = hora_inicial.hour() * 3600 + hora_inicial.minute() * 60 + hora_inicial.second()
        total_segundos_final = hora_final.hour() * 3600 + hora_final.minute() * 60 + hora_final.second()

        # Se a hora final for menor que a inicial, adicionamos 24 horas à final
        if total_segundos_final < total_segundos_inicial:
            total_segundos_final += 24 * 3600

        # Calculando a diferença
        diferenca_segundos = total_segundos_final - total_segundos_inicial

        # Convertendo para horas e minutos
        diferenca_horas = diferenca_segundos // 3600
        diferenca_minutos = (diferenca_segundos % 3600) // 60

        # Formatação para sempre mostrar duas casas em minutos
        total.setText(f"{diferenca_horas}:{diferenca_minutos:02d}")

    def on_calc_km(self,text , km_1, km_2, total):
        total.setText('')
        try:
            valor_1 = km_1.text().replace(',','.')
            valor_2 =  km_2.text().replace(',','.')

            if float(valor_1) > float(valor_2):
                text.setText('valor do km inicial não pode ser maior que o final')
               
                return
            elif valor_1 =='' or valor_2 == '':
                text.setText(f'Campo não pode estar vázio')
                return
            else:
                text.setText(f'')
                r =  float(valor_2) - float(valor_1)
                total.setText(f'{round(r)}')
        except ValueError as e: 
            text.setText(f"{e}")




        pass

    def get_value(self):
        field_frm_diario = DisplayAssociateTable.widget_frm_diario()
        field_frm_entrega = DisplayAssociateTable.widget_frm_entrega()
        try:
            for widget in self.frm_widget_info.findChildren(QWidget):  # Encontra todos os widgets dentro da aba
                    for f in field_frm_diario:
                        if f['requerido'] == True and f['valor_entrada'] == '':
                            
                            return ['Erro',f"{f['descricao_campo']} valor = {f['valor_entrada']}"]
                        
                        else:    
                            if widget.objectName() == f['nome_widget']: 
                                # print(f"{widget.objectName()} == {f['nome_widget']}")      
                                match type(widget).__name__ :
                                    case 'QLineEdit':
                                        if f['tipo_entrada'] == 'float':
                                            if widget.text().strip() != '':
                                                f['valor_entrada'] = float(widget.text().strip().replace(',','.'))
                                            else:
                                                f['valor_entrada'] = float(0)
                                                
                                        elif  f['tipo_entrada'] == 'int':
                                            if widget.text().strip() != '':
                                                f['valor_entrada'] = int(widget.text().strip())
                                            else :  
                                                f['valor_entrada'] = int(0)   
                                                        
                                        else :  
                                            f['valor_entrada'] = widget.text().strip()

                                    case 'QDateEdit':
                                        if widget.text() != '':
                                            f['valor_entrada'] = widget.text().strip()                                       

                                    case 'QCheckBox':
                                        if widget.isChecked():
                                            f['valor_entrada'] = 'S'
                                        else:
                                            f['valor_entrada'] = 'N'   
                                            
                                    case 'QComboBox':
                                        f['valor_entrada'] = widget.currentText()
                                    
                                    case 'QLCDNumber':
                                        f['valor_entrada'] = widget.intValue()    

                                    case 'QPlainTextEdit': 
                                        f['valor_entrada'] = widget.toPlainText()
                                        
                                    case 'QSpinBox': 
                                        f['valor_entrada'] = widget.text().strip()
                                        

                                    case 'QTimeEdit': 
                                        f['valor_entrada'] = widget.text().strip()
                                        
        except ValueError as e: 
            reply = QMessageBox.critical(self, 'Erro ao salvar viagem',
                                     f'Ocorreu um erro ao salvar informação\n Erro: {e}',
                                     QMessageBox.Yes)  

                                       

        for widget in self.frm_widger_entrega.findChildren(QWidget):  # Encontra todos os widgets dentro da aba
                for f in field_frm_entrega:
                    if f['requerido'] == True and f['valor_entrada'] == '':
                        
                        return ['Erro',f"{f['descricao_campo']} valor = {f['valor_entrada']}"]
                    
                    else:    
                        if widget.objectName() == f['nome_widget']: 
                            # print(f"{widget.objectName()} == {f['nome_widget']}")      
                            match type(widget).__name__ :
                                case 'QLineEdit':
                                    if f['tipo_entrada'] == 'float':
                                        if widget.text().strip() != '':
                                            f['valor_entrada'] = float(widget.text().strip().replace(',','.'))
                                        else:
                                            f['valor_entrada'] = float(0)
                                            
                                    elif  f['tipo_entrada'] == 'integer':
                                        if widget.text().strip() != '':
                                            f['valor_entrada'] = int(widget.text().strip())
                                        else :  
                                            f['valor_entrada'] = int(0)

                                    elif f['tipo_entrada']== 'time':

                                        f['valor_entrada'] = widget.text().strip()

                                        pass           
                                                    
                                    else :  
                                        f['valor_entrada'] = widget.text().strip()
                                    
                                case 'QCheckBox':
                                    if widget.isChecked():
                                        f['valor_entrada'] = 'S'
                                    else:
                                        f['valor_entrada'] = 'N'   
                                        
                                case 'QComboBox':
                                    f['valor_entrada'] = widget.currentText()
                                
                                case 'QLCDNumber':
                                    f['valor_entrada'] = widget.intValue()    

                                case 'QPlainTextEdit': 
                                    f['valor_entrada'] = widget.toPlainText()
        return field_frm_diario                             

    def populate_check_box(self):
        
        self.lanc_diario_combobox_app.clear()
        value = Database.get_table_cad_aplicativo()
        for i in value:
            self.lanc_diario_combobox_app.addItem(i[1])

    @Slot() 
    def verify_field(self, read_text:bool = True, enabled_check:bool = False):

        for i in self.field_text:
            if i.isReadOnly() != read_text:
                i.setReadOnly(read_text)

        for e in self.field_check:
            if e.isEnabled() != enabled_check:
                e.setEnabled(enabled_check)

    @Slot() 
    def clear_field(self):

        field = []
        self.lcd_id.setProperty(u"intValue",0)
        for i in self.frm_widget_info.findChildren(QWidget):
            field.append(i)
        for i in self.frm_widger_entrega.findChildren(QWidget):
            field.append(i)

        for i in field:
            if type(i).__name__ == 'QLineEdit' or type(i).__name__ == 'QPlainTextEdit':
                i.clear() 
            elif type(i).__name__ == 'QTimeEdit':
                i.setTime(QTime(0, 0))     



        pass

    @Slot()    
    def callback_bnt_alterar(self):
        
        label_id = self.lcd_id.value()
        if label_id != 0:
            self.lanc_diario_tableView.setEnabled(False)
            self.verify_field(False,True)
            self.disable_tab_widgets(False)
            self.bnt_alterar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_adicionar.setEnabled(False)
            # self.bnt_search.setEnabled(False)
            self.bnt_excluir.setEnabled(False)
            self.modal_seq_info()
            
        else:
            reply = QMessageBox.question(self, 'Error',
                                     'Nenhuma viagem Selecionada',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

            if reply == QMessageBox.Yes:
                self.verify_field(True,False)

    def modal_seq_info(self, form:bool = False):
        self.bnt_back.setEnabled(form)
        self.bnt_back_full.setEnabled(form)
        self.bnt_next.setEnabled(form)
        self.bnt_next_full.setEnabled(form)
    
    @Slot()
    def callback_bnt_incluir(self):
        if self.bnt_alterar.isEnabled() == True:
            self.clear_field()
            self.verify_field(False,True)
            self.lanc_diario_tableView.setEnabled(False)

            self.tableView_2.setEnabled(False)
            

            self.disable_tab_widgets(False)
            self.lanc_diario_date_dia_lanc.setDate(QtCore.QDate.currentDate())
            self.__clear_detalhamento()
            if hasattr(self, 'model_detalhamento') and self.model_detalhamento:
                self.model_detalhamento.clear()
            self.lcd_id.setProperty(u"intValue", 0)
            self.bnt_alterar.setEnabled(False)
            self.bnt_adicionar.setEnabled(False)
            self.bnt_salvar.setEnabled(True)
            self.bnt_excluir.setEnabled(False)
            self.modal_seq_info()
            
    @Slot()
    def callback_bnt_cancela(self):
        label_id = self.lcd_id.value()
        
        if self.bnt_alterar.isEnabled():
            app.closeAllWindows()
            self.destroy()
            

        if label_id == 0:
            self.verify_field()
            self.lanc_diario_tableView.setEnabled(True)
            self.tableView_2.setEnabled(True)
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            # self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.disable_tab_widgets(True)
            self.clear_field()
            # self.populate_field()
            self.modal_seq_info(True)
        else:    
            self.verify_field()
            self.lanc_diario_tableView.setEnabled(True)
            self.bnt_alterar.setEnabled(True)
            self.bnt_salvar.setEnabled(False)
            self.bnt_adicionar.setEnabled(True)
            # self.bnt_search.setEnabled(True)
            self.bnt_excluir.setEnabled(True)
            self.modal_seq_info(True)
            self.disable_tab_widgets(True)

    @Slot()
    def callback_bnt_delete(self):
        value_id = self.lcd_id.intValue()
        if value_id > 0 : 
            reply = QMessageBox.warning(self, 'Excluir',
                                     f'Deseja excluir a viagem de código: {value_id} ?',
                                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            
            if reply == QMessageBox.Yes: 
                delete = Database.delete_entrega_diario(id=value_id)
                
                if delete:
                    reply = QMessageBox.information(self, 'Sucesso',
                                        f'A Viagem de código: {value_id} foi excluida com sucesso',
                                        QMessageBox.Yes)
                    self.clear_field()
                    self.worket.save_data.emit()
                else : 
                    reply = QMessageBox.warning(self, 'erro',
                                        f'Ocorreu um erro ao excluir a viagem:\n {delete[1]}',
                                        QMessageBox.Yes)
                    

    @Slot()
    def callback_bnt_seq_info(self, tipo):
        value_in_db =  Database.get_table_lanc_diario()
        value_id = self.lcd_id.value()
        self.lbl_total.setText(str(len(value_in_db)))
        

        match tipo:
            case "back":
                if value_id == 0:
                    return
                else:
                    if value_id == 0:
                        for i in value_in_db:
                            self.populate_info_diario(id=i)
                            return
                    else:
                        if len(value_in_db) > 1: 

                            a = value_in_db.index(value_id)
                            a -= 1
                            try:
                                b = value_in_db[a]
                                self.populate_info_diario(id=b)
                            except:
                                return   
            
            case "back_full":
                if value_id == 0:
                    return
                else:
                    self.populate_info_diario(id=min(value_in_db))
            
            case "next":
                if value_id == 0:
                    for i in value_in_db:
                        self.populate_info_diario(id=i)
                        return
                else:
                    if len(value_in_db) > 1: 

                        a = value_in_db.index(value_id)
                        a += 1
                        try:
                            b = value_in_db[a]
                            self.populate_info_diario(id=b)
                        except:
                            return    


            case "next_full":
                if value_id == max(value_in_db):
                    return
                else:
                    self.populate_info_diario(id=max(value_in_db))


        pass
    
    @Slot()
    def populate_table_lanc(self, **kwargs):
        data = []

        if 'index_totalizado' in kwargs:
            if hasattr(self, 'model_diario') and self.model_diario:
                self.model_diario.clear()
            if self.combobox_set_totalizado.currentIndex() != 0 :
                data = Database.get_table_lanc_diario(filter=True, tipo = 'data',index_totalizado = self.combobox_set_totalizado.currentIndex())
            else : 
                data = Database.get_table_lanc_diario()

        else :   
            data = Database.get_table_lanc_diario()

        if len(data) > 0:
            headers = ["Código", "App", "Data", "Hora Inicial","Hora Final" ,"Qt Horas", "KM/Lt", "QT Entregas", "Valor Recebido", "OBS"]
            self.model_diario = TableModelSearch(data=data,headers=headers)
            self.lanc_diario_tableView.setModel(self.model_diario)
            self.lbl_total.setText(str(len(data)))
        else :
            if hasattr(self, 'model_diario') and self.model_diario:
                self.model_diario.clear()


    @Slot()
    def populate_table_detalhemento(self,id_lanc:int = 0, **kwargs):
        data = Database.get_table_lanc_detalhamento(tipo = "id", valor = id_lanc)
        # self.model_detalhamento.clear()
        if len(data) > 0 :
            if hasattr(self, 'model_detalhamento') and self.model_detalhamento:
                if 'add_row' not in kwargs:
                    self.model_detalhamento.clear()
            self.model_detalhamento =  TableModelDetalhamento(data=data)
            self.tableView_2.setModel(self.model_detalhamento)
        else :
            if hasattr(self, 'model_detalhamento') and self.model_detalhamento:
                if 'add_row' not in kwargs:
                    self.model_detalhamento.clear()


        if 'add_row' in kwargs:
            if hasattr(self, 'model_detalhamento') and self.model_detalhamento:
             self.model_detalhamento.add_row(kwargs['data'])    
            else:
                self.model_detalhamento =  TableModelDetalhamento(data=data)
                self.model_detalhamento.add_row(kwargs['data']) 
                self.tableView_2.setModel(self.model_detalhamento)
                
           
    def get_all_data(self,model):
        all_data = []
        for row in range(model.rowCount()):
            row_data = []
            for column in range(model.columnCount()):
                index = model.index(row, column)
                data = model.data(index, Qt.ItemDataRole.DisplayRole)
                row_data.append(data)
            all_data.append(row_data)
        return all_data


    def __clear_detalhamento(self):
        field = []
        self.row_table_detalhamento = ""
        self.lcdNumber.setProperty(u"intValue",0)
        for i in self.frm_widger_entrega.findChildren(QWidget):
            field.append(i)
        
        for i in field:
            if type(i).__name__ == 'QLineEdit' or type(i).__name__ == 'QPlainTextEdit':
                i.clear()
            elif type(i).__name__ == 'QTimeEdit':
                i.setTime(QTime(0, 0)) 

    @Slot()
    def show_message(self, title: str = "", text: str = "", *args):
        # Criação da QMessageBox com título e mensagem
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(title)
        msg_box.setText(text)
        
        # Dicionário para armazenar a referência dos botões
        buttons = {}

        # Adiciona cada botão fornecido em args e guarda a referência no dicionário
        for i in args:
            button = msg_box.addButton(i, QMessageBox.ActionRole)
            buttons[button] = i  # Armazena a referência do botão e seu texto

        # Adiciona botão de cancelar
        cancelar_button = msg_box.addButton(QMessageBox.Cancel)
        buttons[cancelar_button] = "Cancelar"  # Nome do botão Cancelar

        # Exibindo a mensagem e aguardando a resposta do usuário
        msg_box.exec()

        # Obtém o botão clicado e retorna seu texto ou identificação
        clicked_button = msg_box.clickedButton()
        return buttons.get(clicked_button, "Cancelar")


    @Slot()
    def get_value_detalhamento(self):
        # Lista com os novos dados, no mesmo formato da sua tabela
        nova_linha_empty = [
                "0",  # Código (ou outra identificação)
                self.lanc_entrega_time_hora_inicial_2.time().toString("HH:mm"),
                self.lanc_entrega_time_hora_final_2.time().toString("HH:mm"),
                self.lanc_entrega_text_qt_horas_2.text(),
                self.lanc_entrega_text_km_inicial_3.text(),
                self.lanc_entrega_text_km_final_2.text(),
                self.lanc_entrega_text_km_total_3.text(),
                self.lanc_entrega_text_total_recebido.text().replace(',','.'),
                self.lanc_entrega_plain_obs.toPlainText(),
                self.lanc_entrega_combobox_tp_pagamento.currentIndex(),
            ]
        
        nova_linha_update = [
                    self.lcdNumber.intValue(),  # Código (ou outra identificação)
                    self.lanc_entrega_time_hora_inicial_2.time().toString("HH:mm"),
                    self.lanc_entrega_time_hora_final_2.time().toString("HH:mm"),
                    self.lanc_entrega_text_qt_horas_2.text(),
                    self.lanc_entrega_text_km_inicial_3.text(),
                    self.lanc_entrega_text_km_final_2.text(),
                    self.lanc_entrega_text_km_total_3.text(),
                    self.lanc_entrega_text_total_recebido.text().replace(',','.'),
                    self.lanc_entrega_plain_obs.toPlainText(),
                    self.lanc_entrega_combobox_tp_pagamento.currentIndex(),
            ]
        
        if self.lcdNumber.intValue() == 0 :
            self.populate_table_detalhemento(add_row = True, data=nova_linha_empty)
            self.__clear_detalhamento()

        else :
            msg = self.show_message("Selecione uma Opção","Deseja inserir ou atualizar o Detalhamento?","Atualizar", "Inserir" )
            match msg:
                case "Atualizar":
                    if hasattr(self, 'model_detalhamento') and self.model_detalhamento:
                        self.model_detalhamento.remove_rows([self.row_table_detalhamento])

                    self.populate_table_detalhemento(add_row = True, data=nova_linha_update)
                    self.__clear_detalhamento()
                case "Inserir":
                    self.populate_table_detalhemento(add_row = True, data=nova_linha_empty)
                    self.__clear_detalhamento()

                case "Cancelar":
                    return

                case _:
                    return    



    @Slot()
    def callback_bnt_delete_detalhamento(self):
        if self.row_table_detalhamento == "":
            self.__clear_detalhamento()
        else :
            if hasattr(self, 'model_detalhamento') and self.model_detalhamento:
                    if self.lcdNumber.intValue() == 0 :
                        self.model_detalhamento.remove_rows([self.row_table_detalhamento])
                        self.__clear_detalhamento()
                    else : 
                        reply = QMessageBox.warning(self, 'Excluir',
                                     f'Deseja excluir o detalhamento de código: {self.lcdNumber.intValue()} ?',
                                    QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            
                        if reply == QMessageBox.Yes: 
                            delete = Database.delete_table_detalhamento(cod_detalhe=self.lcdNumber.intValue(), entre_lanc=self.lcd_id.intValue())
                            
                            if delete:
                                reply = QMessageBox.information(self, 'Sucesso',
                                                    f'A Viagem de código: {self.lcdNumber.intValue()} foi excluida com sucesso',
                                                    QMessageBox.Yes)
                                self.model_detalhamento.remove_rows([self.row_table_detalhamento])
                                self.__clear_detalhamento()
                                self.worket.save_data.emit()
                            else : 
                                reply = QMessageBox.warning(self, 'erro',
                                                    f'Ocorreu um erro ao excluir a viagem:\n {delete[1]}',
                                                    QMessageBox.Yes)





        pass

    @Slot()
    def save_detalhamento(self,id_diario:int):
        data_new = []
        data_update = []
        if hasattr(self, 'model_detalhamento') and self.model_detalhamento:
            data_in_table = self.get_all_data(self.model_detalhamento)
            for i in data_in_table: 
                if int(i[0]) == 0: 
                    data_new.append(i)
                else :
                    data_update.append(i)
            insert =  Database.add_data_detalhamento(data=data_new, id_diario=id_diario)   
            update = Database.add_data_detalhamento(tipo='update', data=data_update,id_diario=id_diario)           
        else:
                pass
        
    @Slot()
    def populate_little_info_frame(self,event=None):
        total_viagens =  0
        media_viagens =  0
        media_consumo = 0 
        media_hora = 0
        total_recebido = 0
        media_recebido = 0

        index_combo = self.combobox_set_totalizado.currentIndex()
        self.populate_table_lanc(index_totalizado = index_combo)

        if hasattr(self, 'model_diario') and self.model_diario:
        #    i.id, i.app, i.data_lanc, i.hora_inicial, i.hora_final, i.qt_hora,i.km_lt, i.qt_entregas, i.vlr_recebido, i.obs
                # 0,1,2,3,4,5,6,7,8,9
        #[[6, 'Uber', datetime.date(2024, 11, 25), datetime.time(0, 0), datetime.time(0, 0), None, 0.0, 6, 0.0, None], [7, 'Uber', datetime.date(2024, 11, 25), datetime.time(0, 0), datetime.time(0, 0), None, 0.0, None, 0.0, None], [8, 'Uber', datetime.date(2024, 11, 25), datetime.time(0, 0), datetime.time(0, 0), None, 0.0, None, 0.0, None]]
            qt_registro = self.model_diario.rowCount()
            for i in self.model_diario._data:
                    
                total_viagens += int(0 if i[7] == None or i[7] =='' else i[7])
                total_recebido += float(i[8] if i[8] != "" else 0)
                media_consumo += float(i[6] if i[6] != "" else 0) 

            self.lbl_media_consumo.setText(f"{media_consumo / qt_registro:.2f}".replace('.',',') if media_consumo !=0 else "0")
            self.lbl_media_viagens.setText(f"{total_viagens / qt_registro:.2f}".replace('.',',') if total_viagens != 0 else "0")
            self.lbl_media_vlr_recebido.setText(f"R$ {total_recebido / qt_registro:.2f}".replace('.',',') if total_recebido !=0 else "0")
            self.lbl_total_recebido.setText(f"R$ {total_recebido:.2f}".replace('.',','))
            self.lbl_total_viagens.setText(f"{total_viagens:.2f}".replace('.',','))

    @Slot()
    def populate_little_info_frame_detalhamento(self,event=None):
        total_viagens =  0
        media_viagens =  0
        media_consumo = 0 
        media_hora = 0
        total_recebido = 0
        media_recebido = 0

        # index_combo = self.combobox_set_totalizado.currentIndex()
        # self.populate_table_lanc(index_totalizado = index_combo)

        if hasattr(self, 'model_detalhamento') and self.model_detalhamento:
            qt_registro = self.model_detalhamento.rowCount()
            # print(self.model_detalhamento._data)
            # ["Código","Hora Inicial", "Hora Final", "Qt Horas", "km Inicial", "KM Final", "Km Total", "Valor Recebido", "OBS", "Tipo Pagamento"]
            for i in self.model_detalhamento._data:
                    
                # total_viagens += int(0 if i[7] == None or i[7] =='' else i[7])
                # total_recebido += float(i[8] if i[8] != "" else 0)
                total_recebido += float(0 if i[7] == None or i[7] =='' else i[7])
                media_consumo += 0 #float(i[6] if i[6] != "" else 0) 

            # self.lbl_media_viagens_detalhamento.setText(f"{total_viagens / qt_registro:.2f}".replace('.',',') if total_viagens != 0 else "0")
            self.lbl_media_vlr_recebido_detalhamento.setText(f"R$ {total_recebido / qt_registro:.2f}".replace('.',',') if total_recebido !=0 else "0")
            self.lbl_total_recebido_detalhamento.setText(f"R$ {total_recebido:.2f}".replace('.',','))
            self.lbl_total_viagens_detalhamento.setText(f"{qt_registro}".replace('.',','))
    @Slot()
    def populate_info_diario(self, *args, **kwargs):

        if self.frm_widget_info.isEnabled()  or self.frm_widger_entrega.isEnabled():
            reply = QMessageBox.question(self, 'Error',
                                     'Objeto em Modo de edição',
                                     QMessageBox.Yes)
            return

        if "id" in kwargs:
            value = Database.get_table_lanc_diario(filter=True, tipo="id",valor=kwargs['id'])[0]


        self.lcd_id.setProperty(u"intValue", value[0])
        self.lanc_diario_combobox_app.setCurrentText(value[1])
        self.lanc_diario_date_dia_lanc.setDate(value[2])
        self.lanc_diario_time_hora_inicial.setTime(value[3])
        self.lanc_diario_time_hora_final.setTime(value[4])
        try:
            self.lanc_diario_text_qt_horas.setText(value[5].strftime('%H:%M'))
        except : 
            self.lanc_diario_text_qt_horas.setText("")
            pass    
        self.lanc_diario_text_media_lt.setText(str(value[6]))
        try:
            self.lanc_diario_spinbox_entregas.setValue(value[7])
        except:
            self.lanc_diario_spinbox_entregas.setValue(0)
            pass   
        self.lanc_diario_text_total_recebido.setText(str(value[8]))
        self.lanc_diario_plain_obs.setPlainText(value[9])
        self.lanc_diario_text_km_inicial.setText(str(value[10]))
        self.lanc_diario_text_km_final.setText(str(value[11]))
        self.lanc_diario_text_km_total.setText(str(value[12]))

    @Slot()
    def populate_field_detalhamento(self, cod :int = 0, lanc_id :int = 0, *args, **kwargs):
        data_info = ""
        self.row_table_detalhamento = kwargs['index_row']
        if cod == str(0):
            if 'data' in kwargs:
                data_info = kwargs['data']
            else :
                data_info = []
        else : 
            data_info =  Database.get_table_lanc_detalhamento(filter=True,tipo='id', valor =lanc_id , valor_cod_detalhe=cod)

        # print(f"{data_info}\n {cod},\n {lanc_id},\n {kwargs['data']}")
        # [i.cod_detalha,i.hora_inicial,i.hora_final,i.qt_hora,i.km_inicial,i.km_final, i.km_total, i.vlr_recebido, i.obs]
        if len(data_info) > 0 :

            if cod != str(0):
                data_info =  data_info[0]
                qt_hora = str(data_info[3]) 
                qt_hora = qt_hora[:5]
                self.lanc_entrega_time_hora_inicial_2.setTime(data_info[1])
                self.lanc_entrega_time_hora_final_2.setTime(data_info[2])

            else :
                self.lanc_entrega_time_hora_inicial_2.setTime(datetime.strptime(data_info[1], "%H:%M").time())
                self.lanc_entrega_time_hora_final_2.setTime(datetime.strptime(data_info[2], "%H:%M").time())
                qt_hora = str(data_info[3]) 

            self.lcdNumber.setProperty(u"intValue", data_info[0])
            
            
            self.lanc_entrega_text_qt_horas_2.setText(str(qt_hora))
            self.lanc_entrega_text_km_inicial_3.setText(str(data_info[4]))
            self.lanc_entrega_text_km_final_2.setText(str(data_info[5]))
            self.lanc_entrega_text_km_total_3.setText(str(data_info[6]))
            self.lanc_entrega_text_total_recebido.setText(str(data_info[7]))
            self.lanc_entrega_plain_obs.setPlainText(data_info[8])
            self.lanc_entrega_combobox_tp_pagamento.setCurrentIndex(data_info[9])
      

        pass

    @Slot()
    def callback_click_row_table_diario(self,index):
        row = index.row()
        row_data = [self.model_diario.data(self.model_diario.index(row, col), Qt.DisplayRole) for col in range(self.model_diario.columnCount(None))]
        self.populate_info_diario(id=row_data[0])
        self.__clear_detalhamento()
        self.populate_table_detalhemento(id_lanc=row_data[0])
        self.populate_little_info_frame_detalhamento()

    def callback_click_row_table_detalhamento(self,index):
        row = index.row()
        row_data = [self.model_detalhamento.data(self.model_detalhamento.index(row, col), Qt.DisplayRole) for col in range(self.model_detalhamento.columnCount(None))]

        self.populate_field_detalhamento(cod=row_data[0],lanc_id=self.lcd_id.intValue(), index_row = row, data = row_data)

    @Slot()
    def closeEvent(self, event,t=None):

        reply = QMessageBox.question(self, 'Confirmar Saída',
                                     'Você realmente fechar o Sistema?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()  # Aceita o fechamento da janela
            self.destroy()

if __name__ == "__main__":
    if sys.platform == "win32":
        import ctypes
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)    

    app = QApplication(sys.argv)
    # window = MainWindow()
    window =  BootingSystem(Worket())
    # window = MainWindow(user='admin',worket=Worket())
    # window =  LancAbastecimento(Worket)
    # app.setStyleSheet(qdarktheme.load_stylesheet(SELECT_THEMA_INI))
  
    window.show()
    sys.exit(app.exec())
