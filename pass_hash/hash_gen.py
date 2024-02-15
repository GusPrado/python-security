import hashlib

text_to_hash = input('Digite o texto para gerar o Hash: ')

menu = int(input('''
            ###### ESCOLHA O TIPO DE HASH ######
            1) MD5
            2) SHA1
            3) SHA256
            4) SHA512
            
            DIGITE O NUMERO CORRESPONDENTE: 
            '''))

if menu == 1:
    result = hashlib.md5(text_to_hash.encode('utf-8'))
    print("HASH MD5", result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(text_to_hash.encode('utf-8'))
    print("HASH SHA1", result.hexdigest())
elif menu == 3:
    result = hashlib.sha256(text_to_hash.encode('utf-8'))
    print("HASH SHA256", result.hexdigest())
elif menu == 4:
    result = hashlib.sha512(text_to_hash.encode('utf-8'))
    print("HASH SHA512", result.hexdigest())
else:
    print('Algo de errado não está certo. Tente novamente.')
