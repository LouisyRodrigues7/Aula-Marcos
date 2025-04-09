class Empresa:
    
    pilares = []
    nome = "Turma 34"
    funcionarios = []
    
    def cadastrar_pilares(self,nome,descricao):
        self.pilares.append((nome,descricao))
        
        
    def consultar_pilares(self):
        for p in self.pilares:
            print(f"Pilar: {p[0]}, Descrição: {p[1]}")
    
    def cadastrar_fincionario(self,nome,salario):
        self.funcionarios.append((nome,salario))
        
    def consultar_funcionarios(self):
        for f in self.funcionarios:
            print(f"Funcionário: {f[0]}, Salário: {f[1]}")
            
emp = Empresa()
emp.cadastrar_pilares("Ética", "Agir eticamente")
print(emp.pilares)
    