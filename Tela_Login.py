import json
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox,  QMainWindow, QWidget
from tela_registro import TelaRegistro

usuario_logado = None

class TelaLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label_usuario = QLabel("Usuário:")
        self.input_usuario = QLineEdit()
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)

        self.label_senha = QLabel("Senha:")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.input_senha)

        self.botao_login = QPushButton("Login")
        self.botao_login.clicked.connect(self.verificar_login)
        layout.addWidget(self.botao_login)

        # Botão de Registrar
        self.botao_registrar = QPushButton("Registrar")
        self.botao_registrar.clicked.connect(self.abrir_tela_registro)
        layout.addWidget(self.botao_registrar)

        self.setLayout(layout)

    def resetar_campos(self):
        """Método para limpar os campos de login"""
        self.input_usuario.clear()
        self.input_senha.clear()

    def abrir_tela_registro(self):
        # Método que abre a tela de registro
        self.tela_registro = TelaRegistro()  
        self.tela_registro.exec_()  

    def verificar_login(self):
        usuario = self.input_usuario.text()
        senha = self.input_senha.text()
        pass

        try:
            with open("usuarios.json", "r") as arquivo:
                dados = json.load(arquivo)
                for u in dados["usuarios"]:
                    if u["usuario"] == usuario and u["senha"] == senha:
                        QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
                        self.accept()
                        return
            QMessageBox.warning(self, "Erro", "Usuário ou senha inválidos!")
        except FileNotFoundError:
            QMessageBox.critical(self, "Erro", "Arquivo de usuários não encontrado!")

    
    
        
