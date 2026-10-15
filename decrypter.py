from cryptography.fernet import Fernet

# Descriptografa o conteúdo de um arquivo
def descriptografar(arquivo):
    with open("chave.key", "rb") as chave_file:
        chave = chave_file.read()
    f = Fernet(chave)
    with open(arquivo, "rb") as file:
        dados_encriptados = file.read()
    dados = f.decrypt(dados_encriptados)
    with open(arquivo, "wb") as file:
        file.write(dados)

# Exemplo de uso
descriptografar("teste.txt")
