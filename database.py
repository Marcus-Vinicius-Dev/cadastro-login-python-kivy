import datetime

class DataBase():
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        self.usuarios = None
        self.arquivo = None
        self.load()
        
    def load(self):
        self.arquivo = open(self.nome_arquivo, "r")
        self.usuarios = {}
        
        for linha in self.arquivo:
            email, senha, nome, criado_em= linha.strip().split(";")
            self.usuarios[email] = (senha, nome, criado_em)
            
        self.arquivo.close()
        
    def pegar_usuario(self, email):
        if email in self.usuarios:
            return self.usuaios[email]
        else:
            return -1
        
    def validar(self, email, senha, nome):
        if email.strip() not in self.usuarios:
            self.usuarios[email.strip()] = (senha.strip(), nome.strip(), DataBase.get_date())
            self.salvar()
            return 1
        else:
            print("Email ja existe!")
            return -1
    
    def salvar(self):
        with open(self.arquivo, "w") as f:
            for usuario in self.usuarios:
                f.write(usuario + ";" + self.usuarios[usuario][0] + ";" + self.usuarios[usuario][1] + ";" + self[usuario][2] + "\n")
                
    
    @staticmethod
    def pegar_data():
        return str(datetime.datetime.now()).split(" ")[0]