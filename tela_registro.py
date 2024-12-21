import json
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class TelaRegistro(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrar Usuário")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label_usuario = QLabel("Novo Usuário:")
        self.input_usuario = QLineEdit()
        layout.addWidget(self.label_usuario)
        layout.addWidget(self.input_usuario)

        self.label_senha = QLabel("Nova Senha:")
        self.input_senha = QLineEdit()
        self.input_senha.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.label_senha)
        layout.addWidget(self.input_senha)

        self.botao_registrar = QPushButton("Registrar")
        self.botao_registrar.clicked.connect(self.registrar_usuario)
        layout.addWidget(self.botao_registrar)

        self.setLayout(layout)

    def registrar_usuario(self):
        novo_usuario = self.input_usuario.text()
        nova_senha = self.input_senha.text()

        if not novo_usuario or not nova_senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos!")
            return

        try:
            with open("usuarios.json", "r") as arquivo:
                dados = json.load(arquivo)

            # Verifica se o usuário já existe
            for u in dados["usuarios"]:
                if u["usuario"] == novo_usuario:
                    QMessageBox.warning(self, "Erro", "Usuário já existe!")
                    return

            # Adiciona o novo usuário
            dados["usuarios"].append({"usuario": novo_usuario, "senha": nova_senha})

            # Salva no arquivo JSON
            with open("usuarios.json", "w") as arquivo:
                json.dump(dados, arquivo, indent=4)

            QMessageBox.information(self, "Sucesso", "Usuário registrado com sucesso!")
            self.accept()
        except FileNotFoundError:
            QMessageBox.critical(self, "Erro", "Arquivo de usuários não encontrado!")
        except json.JSONDecodeError:
            QMessageBox.critical(self, "Erro", "Erro ao ler o arquivo de dados!")
