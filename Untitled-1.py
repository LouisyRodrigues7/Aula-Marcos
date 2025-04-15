# Integridade conceitual: manter o design uniforme e fácil de entender.
# Ocultamento de informação: proteger os dados internos da classe.
# Alta coesão: cada classe com uma única responsabilidade clara.
# Baixo acoplamento: reduzir a dependência entre partes do código.

# os atributos estão protegidos por _ e só são acessados por métodos.
# Pilar e Funcionario cuidam de suas próprias informações.
# Empresa usa as outras classes, mas sem se prender aos seus detalhes internos.
# mais modular e fácil de manter.

class Pilar:
    def __init__(self, nome: str, descricao: str):
        self._nome = nome
        self._descricao = descricao

    def __str__(self):
        return f"Pilar: {self._nome}, Descrição: {self._descricao}"

    def get_nome(self):
        return self._nome

    def get_descricao(self):
        return self._descricao


class Funcionario:
    def __init__(self, nome: str, salario: float):
        self._nome = nome
        self._salario = salario

    def __str__(self):
        return f"Funcionário: {self._nome}, Salário: {self._salario:.2f}"

    def get_nome(self):
        return self._nome

    def get_salario(self):
        return self._salario


class Empresa:
    def __init__(self, nome: str):
        self._nome = nome
        self._pilares = []
        self._funcionarios = []

    def cadastrar_pilar(self, nome: str, descricao: str):
        pilar = Pilar(nome, descricao)
        self._pilares.append(pilar)

    def consultar_pilares(self):
        return [str(p) for p in self._pilares]

    def cadastrar_funcionario(self, nome: str, salario: float):
        funcionario = Funcionario(nome, salario)
        self._funcionarios.append(funcionario)

    def consultar_funcionarios(self):
        return [str(f) for f in self._funcionarios]

    def get_nome(self):
        return self._nome
    
    # Testando
if __name__ == "__main__":
    emp = Empresa("Turma 34")
    emp.cadastrar_pilar("Ética", "Agir eticamente")
    emp.cadastrar_funcionario("João", 3000)

    print("Pilares:")
    for p in emp.consultar_pilares():
        print(p)

    print("\nFuncionários:")
    for f in emp.consultar_funcionarios():
        print(f)