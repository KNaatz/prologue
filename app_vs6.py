from PyQt5.QtWidgets import QMessageBox, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QFormLayout, QLineEdit, QComboBox, QDialog, QDialogButtonBox, QMainWindow
import sys
import json
from Tela_Login import TelaLogin


class JanelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicativo Principal")
        self.setGeometry(100, 100, 800, 600)

app = QApplication(sys.argv)

#Tela de Login
tela_login = TelaLogin
janela_principal = None

def fazer_logoff():
        global janela_principal
        resposta = QMessageBox.question(
            None,
            "Confirmar Log Off",
            "Tem certeza que quer sair da conta?",
            QMessageBox.Yes | QMessageBox.No
            )
        
        if resposta == QMessageBox.Yes:
            if janela_principal: 
             janela_principal.close()
             janela_principal= None

            tela_login.resetar_campos()
            tela_login.show()

tela_login = TelaLogin()
if tela_login.exec_() == QDialog.accepted:
    janela_principal = JanelaPrincipal()
    janela_principal.show()
    sys.exit(app.exec_())

# Função para preencher a tabela com dados iniciais
def preencher_tabela():
    dados = [
        ("Game of Thrones", "J.R.R. Tolkien", "Ficção Científica", "49.9", "50"),
        ("O Senhor dos Anéis", "Neil Gaiman", "Fantasia", "59.9", "30"),
        ("Coraline", "George R.R. Martin", "Fantasia", "39.9", "40"),
    ]
    
    for linha, livro in enumerate(dados):
        for coluna, valor in enumerate(livro):
            tabela.setItem(linha, coluna, QTableWidgetItem(valor))

# Função para adicionar um novo livro
def adicionar_livro():
    dialogo = QDialog()
    dialogo.setWindowTitle("Adicionar Novo Livro")

    # Layout do formulário
    formulario = QFormLayout()

    # Campos de entrada
    campo_titulo = QLineEdit()
    campo_autor = QLineEdit()
    campo_genero = QComboBox()
    campo_genero.addItems(["Ficção Científica", "Romance", "Fantasia", "Mistério", "Aventura", "Terror"])
    campo_preco = QLineEdit()
    campo_estoque = QLineEdit()

    # Adicionando os campos ao layout
    formulario.addRow("Título", campo_titulo)
    formulario.addRow("Autor", campo_autor)
    formulario.addRow("Gênero", campo_genero)
    formulario.addRow("Preço", campo_preco)
    formulario.addRow("Estoque", campo_estoque)

    # Botões de confirmação
    botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    formulario.addWidget(botoes)

    # Conectar os botões para aceitar ou cancelar a inserção
    botoes.accepted.connect(dialogo.accept)
    botoes.rejected.connect(dialogo.reject)

    dialogo.setLayout(formulario)

    if dialogo.exec_() == QDialog.Accepted:
        # Coletar dados inseridos no formulário
        titulo = campo_titulo.text()
        autor = campo_autor.text()
        genero = campo_genero.currentText()
        preco = campo_preco.text()
        estoque = campo_estoque.text()

        # Adicionar na tabela
        row_position = tabela.rowCount()
        tabela.insertRow(row_position)
        tabela.setItem(row_position, 0, QTableWidgetItem(titulo))
        tabela.setItem(row_position, 1, QTableWidgetItem(autor))
        tabela.setItem(row_position, 2, QTableWidgetItem(genero))
        tabela.setItem(row_position, 3, QTableWidgetItem(preco))
        tabela.setItem(row_position, 4, QTableWidgetItem(estoque))


#Função para deletar livro:
def deletar_livro():
    linha_selecionada = tabela.currentRow()

    if linha_selecionada != -1:
        resposta = QMessageBox.question(
            janela,
            'Excluir Livro',
            'Você tem certeza que deseja excluir este livro?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
    if resposta == QMessageBox.Yes:
        tabela.removeRow(linha_selecionada)
    
    else: 
        QMessageBox.warning(janela, 'Erro', 'Nenhum livro selecionado para excluir.')


#Função para editar livro.
def editar_livro():
    linha_selecionada = tabela.currentRow()

    if linha_selecionada == -1:
        QMessageBox.warning(janela, 'Erro', 'Nenhum livro selecionado para editar.')
        return

    # Criar o diálogo de edição
    dialogo = QDialog()
    dialogo.setWindowTitle("Editar Livro")
    formulario = QFormLayout()

    # Obter valores da linha selecionada
    titulo_atual = tabela.item(linha_selecionada, 0).text()
    autor_atual = tabela.item(linha_selecionada, 1).text()
    genero_atual = tabela.item(linha_selecionada, 2).text()
    preco_atual = tabela.item(linha_selecionada, 3).text()
    estoque_atual = tabela.item(linha_selecionada, 4).text()

    # Campos de entrada preenchidos com valores atuais
    campo_titulo = QLineEdit(titulo_atual)
    campo_autor = QLineEdit(autor_atual)
    campo_genero = QComboBox()
    campo_genero.addItems(["Ficção Científica", "Romance", "Fantasia", "Mistério", "Aventura", "Terror"])
    campo_genero.setCurrentText(genero_atual)
    campo_preco = QLineEdit(preco_atual)
    campo_estoque = QLineEdit(estoque_atual)

    # Adicionar os campos ao formulário
    formulario.addRow("Título", campo_titulo)
    formulario.addRow("Autor", campo_autor)
    formulario.addRow("Gênero", campo_genero)
    formulario.addRow("Preço", campo_preco)
    formulario.addRow("Estoque", campo_estoque)

    # Botões de confirmação
    botoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
    formulario.addWidget(botoes)

    # Conectar os botões para aceitar ou rejeitar
    botoes.accepted.connect(dialogo.accept)
    botoes.rejected.connect(dialogo.reject)

    dialogo.setLayout(formulario)

    # Executar o diálogo e, se aceito, salvar as alterações
    if dialogo.exec_() == QDialog.Accepted:
        tabela.setItem(linha_selecionada, 0, QTableWidgetItem(campo_titulo.text()))
        tabela.setItem(linha_selecionada, 1, QTableWidgetItem(campo_autor.text()))
        tabela.setItem(linha_selecionada, 2, QTableWidgetItem(campo_genero.currentText()))
        tabela.setItem(linha_selecionada, 3, QTableWidgetItem(campo_preco.text()))
        tabela.setItem(linha_selecionada, 4, QTableWidgetItem(campo_estoque.text()))

#Função para Salvar os dados da tabela em um arquivo JSON
def salvar_dados_em_json():
    dados = []
    for linha in range (tabela.rowCount()):
        livro = {
            "Título": tabela.item(linha, 0).text(),
            "Autor": tabela.item(linha, 1).text(),
            "Gênero": tabela.item(linha, 2).text(),
            "Preço": tabela.item(linha, 3).text(),
            "Estoque": tabela.item(linha, 4).text()
        }
        dados.append(livro)

    with open("livraria_dados.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
    QMessageBox.information(janela, "Sucesso", "Dados salvos com sucesso!")

#Função para carregar os dados do arquivo JSON;
def carregar_dados_de_json():
    try:
        with open("livraria_dados.json", "r") as arquivo:
            dados = json.load(arquivo)
        tabela.setRowCount(0)  # Limpar a tabela antes de carregar
        for livro in dados:
            row_position = tabela.rowCount()
            tabela.insertRow(row_position)
            tabela.setItem(row_position, 0, QTableWidgetItem(livro["Título"]))
            tabela.setItem(row_position, 1, QTableWidgetItem(livro["Autor"]))
            tabela.setItem(row_position, 2, QTableWidgetItem(livro["Gênero"]))
            tabela.setItem(row_position, 3, QTableWidgetItem(livro["Preço"]))
            tabela.setItem(row_position, 4, QTableWidgetItem(livro["Estoque"]))
    except FileNotFoundError:
        QMessageBox.warning(janela, "Aviso", "Nenhum arquivo de dados encontrado. A tabela está vazia.")
    except json.JSONDecodeError:
        QMessageBox.critical(janela, "Erro", "Erro ao carregar o arquivo de dados. Verifique o formato do JSON.")



# Janela principal
janela = QWidget()
janela.setWindowTitle('Prologue')
janela.setGeometry(100, 100, 800, 600)

# Layout principal
layout_principal = QHBoxLayout()

# Layout do menu
menu_layout = QVBoxLayout()
btn_adicionar = QPushButton("Adicionar Livro")
btn_editar = QPushButton("Editar Livro")
btn_deletar = QPushButton("Deletar Livro")
menu_layout.addWidget(btn_adicionar)
menu_layout.addWidget(btn_editar)
menu_layout.addWidget(btn_deletar)
menu_layout.addStretch()

# Tabela
tabela = QTableWidget()
tabela.setRowCount(3)
tabela.setColumnCount(5)
tabela.setHorizontalHeaderLabels(["Título", "Autor", "Gênero", "Preço", "Estoque"])

#Botões Logoff
botao_logoff = QPushButton("Log Off")
botao_logoff.clicked.connect(fazer_logoff)
botao_logoff.setGeometry(250, 200, 100, 40)
menu_layout.addWidget(botao_logoff)

# Preencher a tabela com dados iniciais
preencher_tabela()

# Conectar o botão "Adicionar Livro" à função de adicionar livro
btn_adicionar.clicked.connect(adicionar_livro)

# Conectar o botão "Deletar Livro" com a função deletar livro
btn_deletar.clicked.connect(deletar_livro)

# Conectar o botão "Editar" com a função Editar Livro
btn_editar.clicked.connect(editar_livro)

#Conectar a função de salvar ao botão.
btn_salvar = QPushButton("Salvar Dados")
btn_salvar.clicked.connect(salvar_dados_em_json)
menu_layout.addWidget(btn_salvar)

# Adicionar o layout do menu e da tabela ao layout principal
layout_principal.addLayout(menu_layout)
layout_principal.addWidget(tabela)

# Definir o layout da janela principal
janela.setLayout(layout_principal)

#Carregar dados;
carregar_dados_de_json()

# Mostrar a janela principal
janela.show()

sys.exit(app.exec_())
