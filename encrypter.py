from cryptography.fernet import Fernet

# Gera uma chave e salva em um arquivo
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as chave_file:
        chave_file.write(chave)

# Criptografa o conteúdo de um arquivo
def criptografar(arquivo):
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados = file.read()
    dados_encriptados = f.encrypt(dados)
    with open(arquivo, "wb") as file:
        file.write(dados_encriptados)

# Exemplo de uso
gerar_chave()
criptografar("teste.txt")
