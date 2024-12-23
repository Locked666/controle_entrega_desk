import os 
import sys
from pathlib import Path


class DisplayAssociateTable():
    def __init__(self):
        pass

    def widget_frm_diario():
        widget = [
                # {'tipo': 'QLCDNumber', 'nome_widget': 'lcd_id','valor_entrada':'','tabela': 'produtos','campo': 'id','requerido' : False},
                {'tipo': 'QLineEdit', 'nome_widget': 'lanc_diario_text_media_lt', 'tipo_entrada' : 'float', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'km_lt','object':None ,'requerido': False}, 
                {'tipo': 'QSpinBox', 'nome_widget': 'lanc_diario_spinbox_entregas', 'tipo_entrada' : 'int', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'qt_entregas','object':None ,'requerido': False}, 
                {'tipo': 'QSpinBox', 'nome_widget': 'lanc_diario_text_total_recebido', 'tipo_entrada' : 'float', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'vlr_recebido','object':None ,'requerido': False}, 
                # {'tipo': 'QLineEdit', 'nome_widget': 'lanc_diario_text_total_recebido', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': '', 'campo': '','object':None ,'requerido': False}, 
                {'tipo': 'QPlainTextEdit', 'nome_widget': 'lanc_diario_plain_obs', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'obs','object':None ,'requerido': False}, 
                {'tipo': 'QComboBox', 'nome_widget': 'lanc_diario_combobox_app', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'app','object':None ,'requerido': False}, 
                {'tipo': 'QDateEdit', 'nome_widget': 'lanc_diario_date_dia_lanc', 'tipo_entrada' : 'date', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'data_lanc','object':None ,'requerido': False}, 
                {'tipo': 'QTimeEdit', 'nome_widget': 'lanc_diario_time_hora_inicial', 'tipo_entrada' : 'time', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'hora_inicial','object':None ,'requerido': False}, 
                {'tipo': 'QLineEdit', 'nome_widget': 'lanc_diario_text_km_inicial', 'tipo_entrada' : 'float', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'km_inicial','object':None ,'requerido': False}, 
                {'tipo': 'QTimeEdit', 'nome_widget': 'lanc_diario_time_hora_final', 'tipo_entrada' : 'time', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'hora_final','object':None ,'requerido': False}, 
                {'tipo': 'QLineEdit', 'nome_widget': 'lanc_diario_text_km_final', 'tipo_entrada' : 'float', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'km_final','object':None ,'requerido': False}, 
                {'tipo': 'QLineEdit', 'nome_widget': 'lanc_diario_text_qt_horas', 'tipo_entrada' : 'time', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'qt_hora','object':None ,'requerido': False}, 
                {'tipo': 'QLineEdit', 'nome_widget': 'lanc_diario_text_km_total', 'tipo_entrada' : 'float', 'valor_entrada': '', 'tabela': 'lanc_entrega', 'campo': 'km_total','object':None ,'requerido': False}
                ]
        return widget

    def widget_frm_entrega():
        widget = [
            {'tipo': 'QPlainTextEdit', 'nome_widget': 'lanc_entrega_plain_obs', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QPushButton', 'nome_widget': 'lanc_entrega_bnt_add', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QPushButton', 'nome_widget': 'lanc_entrega_bnt_delete', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QTimeEdit', 'nome_widget': 'lanc_entrega_time_hora_inicial_2', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QTimeEdit', 'nome_widget': 'lanc_entrega_time_hora_final_2', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QLineEdit', 'nome_widget': 'lanc_entrega_text_qt_horas_2', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QLineEdit', 'nome_widget': 'lanc_entrega_text_km_inicial_3', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QLineEdit', 'nome_widget': 'lanc_entrega_text_km_final_2', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QLineEdit', 'nome_widget': 'lanc_entrega_text_km_total_3', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}, 
            {'tipo': 'QLineEdit', 'nome_widget': 'lanc_entrega_text_km_total_4', 'tipo_entrada' : 'str', 'valor_entrada': '', 'tabela': 'lanc_entrega_item', 'campo': '', 'object': None, 'requerido': False}]
        
        return widget  


if __name__=='__main__'    :
    pass