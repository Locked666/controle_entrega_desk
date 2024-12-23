from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow

class PDFReport:
    def __init__(self, filename):
        self.filename = filename

    def create_pdf(self, data):
        pdf = SimpleDocTemplate(self.filename, pagesize=A4)
        elements = []

        # Estilos para o PDF
        styles = getSampleStyleSheet()
        title_style = styles["Title"]
        header_style = styles["Heading2"]
        normal_style = styles["BodyText"]

        # Adicionando cabeçalho
        elements.append(Paragraph("Relatório de Viagem", title_style))
        elements.append(Paragraph("Detalhes das Viagens", header_style))

        # Dados da tabela (exemplo)
        table_data = [["Código", "Descrição", "Data", "Status"]] + data

        # Estilo da tabela
        table = Table(table_data, colWidths=[3 * cm, 6 * cm, 3 * cm, 3 * cm])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)

        # Construindo o PDF
        pdf.build(elements)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gerar Relatório em PDF")
        self.setGeometry(100, 100, 300, 200)

        button = QPushButton("Gerar Relatório", self)
        button.clicked.connect(self.generate_report)
        button.setGeometry(75, 80, 150, 40)

    def generate_report(self):
        # Dados fictícios para o relatório
        data = [
            ["001", "Viagem de São Paulo a Rio de Janeiro", "2024-11-12", "Concluída"],
            ["002", "Viagem de Porto Alegre a Curitiba", "2024-11-13", "Pendente"],
            ["003", "Viagem de Brasília a Salvador", "2024-11-14", "Cancelada"],
        ]

        # Geração do relatório em PDF
        report = PDFReport("relatorio_viagem.pdf")
        report.create_pdf(data)

        print("Relatório PDF gerado com sucesso!")

# Execução da aplicação PySide6
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
