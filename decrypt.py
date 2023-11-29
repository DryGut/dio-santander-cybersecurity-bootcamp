import os
import pyaes as hash

file_name = 'teste.txt.pwned'
        
def abre_arquivo_cripto(file_name):
    with open(file_name, 'rb') as file:
        file_data = file.read()
        key = b'temdesesseisletr'
        aes = hash.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)
    return decrypt_data  
        
    
def cria_novo_arquivo(data):
    new_file = 'teste.txt'
    with open(new_file, 'wb') as new:
        new.write(data)

if __name__ == '__main__':
    arquivo = abre_arquivo_cripto(file_name)
    os.remove('teste.txt.pwned')
    cria_novo_arquivo(arquivo)