import datetime


class Pessoa:
    # __renda = None
    __nome = None
    __sexo = None
    __data_nascimento = None

    def __init__(self, nome,  sexo, data_nascimento):  # Construtor / Visbilidade (atributos publicos)
        self.set_nome(nome)
        self.set_sexo(sexo)
        self.set_data_nascimento(data_nascimento)

    def set_nome(self, nome):
        self.__nome = nome
    
    def get_nome(self):
        return self.__nome

    def set_sexo(self, sexo):
        self.__sexo = sexo
    
    def get_sexo(self):
        return self.__sexo
    
    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento
    
    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_idade(self):
        idade = int(datetime.datetime.now().year) - int(datetime.date.replace(self.data_nascimento).year)
        return idade

    # def set_renda(self, valor):
    #     self.__renda = valor

    # def get_renda(self):
    #     return self.__renda