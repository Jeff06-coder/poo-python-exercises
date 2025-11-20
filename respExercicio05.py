
class Pessoa:
    def __init__(self, nome, cpf, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

    def apresentar(self):
         return(f"Olá, meu nome é {self.nome} e tenho {self.data_nascimento} de nacimento.")
    
class Funcionario(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, cargo, salario):
        super().__init__(nome, cpf, data_nascimento)
        self.cargo = cargo
        self.salario = salario

    def apresentar(self):
        return(f"Olá, meu nome é {self.nome}, tenho {self.cpf} de nacimento e trabalho como {self.cargo}.")
    
    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("CPF: ", self.cpf,)
        print("Data: ", self.data_nascimento)
        print("Cargo: ", self.cargo)
        print("Salário: ", self.salario)
        


class Tutor(Pessoa):
    def __init__(self, nome, cpf, data_nascimento, area_atuacao):
        super().__init__(nome, cpf, data_nascimento)
        self.area_atuacao = area_atuacao

    def apresentar(self):
        return(f"Olá, sou {self.nome}, CPF: {self.cpf}, atuo na área de {self.area_atuacao}.")
    

funcionario = Funcionario("Ana Costa", "111.222.333-44", "20/03/1988", "Coordenadora", 4500.0)
funcionario.exibir_dados()