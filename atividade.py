#ALUNAS: Lara de Araujo e Arauna Noemi.

import os
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuração do banco de dados
BANCO_FUNCIONARIOS = create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=BANCO_FUNCIONARIOS)
session = Session()
Base = declarative_base()

class Funcionario(Base):
    __tablename__ = "funcionarios"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    idade = Column(Integer)
    cpf = Column(String)
    setor = Column(String)
    funcao = Column(String)
    salario = Column(Float)
    telefone = Column(String)

    def __init__(self, nome: str, idade: int, cpf: str, setor: str, funcao: str, salario: float, telefone: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.setor = setor
        self.funcao = funcao
        self.salario = salario
        self.telefone = telefone

Base.metadata.create_all(bind=BANCO_FUNCIONARIOS)

def salvar_funcionario(funcionario):
    session.add(funcionario)
    session.commit()

def listar_todos_funcionarios():
    return session.query(Funcionario).all()

def pesquisar_um_funcionario(cpf):
    return session.query(Funcionario).filter(Funcionario.cpf == cpf).first()

def atualizar_funcionario(cpf, novos_dados):
    funcionario = pesquisar_um_funcionario(cpf)
    if funcionario:
        for key, value in novos_dados.items():
            setattr(funcionario, key, value)
        session.commit()

def excluir_funcionario(cpf):
    funcionario = pesquisar_um_funcionario(cpf)
    if funcionario:
        session.delete(funcionario)
        session.commit()

def menu():
    while True:
        print("\n     === RH System ===")
        print("       1 - Adicionar funcionário")
        print("       2 - Consultar um funcionário")
        print("       3 - Atualizar os dados de um funcionário")
        print("       4 - Excluir um funcionário")
        print("       5 - Listar todos os funcionários")
        print("       0 - Sair do sistema.")
        
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            cpf = input("CPF: ")
            setor = input("Setor: ")
            funcao = input("Função: ")
            salario = float(input("Salário: "))
            telefone = input("Telefone: ")
            
            funcionario = Funcionario(nome=nome, idade=idade, cpf=cpf, setor=setor, funcao=funcao, salario=salario, telefone=telefone)
            salvar_funcionario(funcionario)
            print("Funcionário adicionado com sucesso.")
            
        elif escolha == "2":
            cpf = input("Digite o CPF do funcionário: ")
            funcionario = pesquisar_um_funcionario(cpf)

            if funcionario:
                print(f"Funcionário encontrado: Nome: {funcionario.nome}, Idade: {funcionario.idade}, Setor: {funcionario.setor}, Salário: {funcionario.salario}, Telefone: {funcionario.telefone}")
            else:
                print("Funcionário não encontrado.")

        elif escolha == "3":
            cpf = input("Digite o CPF do funcionário a ser atualizado: ")
            novos_dados = {}
            novos_dados['nome'] = input("Novo nome (deixe vazio para não alterar): ") or None
            novos_dados['idade'] = input("Nova idade (deixe vazio para não alterar): ")
            novos_dados['setor'] = input("Novo setor (deixe vazio para não alterar): ") or None
            novos_dados['funcao'] = input("Nova função (deixe vazio para não alterar): ") or None
            novos_dados['salario'] = input("Novo salário (deixe vazio para não alterar): ")
            novos_dados['telefone'] = input("Novo telefone (deixe vazio para não alterar): ") or None

            # Remover chaves com valores vazios
            novos_dados = {k: (int(v) if k == 'idade' else float(v) if k == 'salario' else v) for k, v in novos_dados.items() if v is not None}
            atualizar_funcionario(cpf, novos_dados)
            print("Dados atualizados com sucesso.")

        elif escolha == "4":
            cpf = input("Digite o CPF do usuário a ser excluído: ")
            excluir_funcionario(cpf)
            print("Funcionário excluído com sucesso.")

        elif escolha == "5":
            funcionarios = listar_todos_funcionarios()
            for f in funcionarios:
                print(f"{f.nome}, Idade: {f.idade}, CPF: {f.cpf}, Setor: {f.setor}, Função: {f.funcao}, Salário: {f.salario}, Telefone: {f.telefone}")

        elif escolha == "0":
            print("Saindo do sistema.")
            break

if __name__ == "__main__":
    menu()



      



