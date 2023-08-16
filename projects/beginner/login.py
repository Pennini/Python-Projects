import re
import getpass

usuarios = {}


def cadastrar_usuario(usuarios):
    # Solicite ao usuário que digite um nome de usuário e uma senha
    print("Cadastro\n")
    login = input("Username: ")
    # Verifique se o nome de usuário já existe no dicionário 'usuarios'
    while login in usuarios or len(login) == 0:
        login = input("Este login não é válido, tente outro: ")
    senha = getpass.getpass(
        "Senha precisa ter letras, um caractere especial, um número e 6 caracteres pelo menos.\n Senha: "
    )
    # Armazene o nome de usuário e a senha correspondente no dicionário 'usuarios'
    while not (
        re.search(r"[a-zA-Z]", senha)
        and re.search(r"[!@#$%^&*()]", senha)
        and re.search(r"[0-9]", senha)
        and len(senha) >= 6
    ):
        senha = getpass.getpass("Sua senha não atende aos requisitos, tente outra: ")

    # Armazene o nome de usuário e a senha correspondente no dicionário 'usuarios'
    usuarios[login] = senha
    print(f"Cadastrado com sucesso: {login}")
    return login, senha


def fazer_login(usuarios):
    x = 0
    # Solicite ao usuário que digite seu nome de usuário e senha
    login = input("Login: ")
    # Verifique se o nome de usuário existe no dicionário 'usuarios'
    if login not in usuarios:
        print("Este login não existe")
        x = 1

    if x == 0:
        senha = getpass.getpass("Senha: ")

        # Verifique se a senha fornecida corresponde à senha armazenada
        if usuarios[login] != senha:
            print("Senha incorreta")
            x = 1

    return x


decisao = input(
    "Olá, boas vindas! Deseja fazer login ou se cadastrar?\n1 - Login\n2 - Cadastro\n"
)
while decisao != "1" and decisao != "2":
    decisao = input("Por favor, digite 1 para login ou 2 para cadastro: ")

# Com base na escolha do usuário, chame a função adequada
while decisao == "1":
    x = fazer_login(usuarios)
    repeat = 0
    while x == 1 and repeat < 2:
        x = fazer_login(usuarios)
        repeat += 1
    if x == 1:
        decisao = input(
            "Você ainda não tem cadastro? 1 - Tentar de novo e 2 - Cadastro"
        )
        while decisao != "1" and decisao != "2":
            decisao = input(
                "Por favor, digite 1 para tentar de novo o login ou 2 para cadastro: "
            )
    if x == 0:
        print("Parabéns, você entrou na sua conta!")
        decisao = 0

if decisao == "2":
    cadastrar_usuario(usuarios)
