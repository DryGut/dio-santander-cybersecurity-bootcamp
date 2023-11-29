import os
import pyaes as hash

file_name = 'teste.txt'
        
def abre_arquivo(file_name):
    with open(file_name, 'rb') as file:
        file_data = file.read()
        key = b'temdesesseisletr'
        aes = hash.AESModeOfOperationCTR(key)
        encrypt_data = aes.encrypt(file_data)
    return encrypt_data 
    
def cria_novo_arquivo(data):
    new_file = file_name + '.pwned'
    with open(new_file, 'wb') as new:
        new.write(data)

if __name__ == '__main__':
    arquivo = abre_arquivo(file_name)
    os.remove('teste.txt')
    cria_novo_arquivo(arquivo)