import hashlib

file1 = '/Users/gusprado/dev/dio/python_dev_formation/security/python-security/pass_hash/files_2_compare/a.txt'
file2 = '/Users/gusprado/dev/dio/python_dev_formation/security/python-security/pass_hash/files_2_compare/b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print('Arquivos diferentes')
    print(f'Hash 1: {hash1.hexdigest()}')
    print(f'Hash 2: {hash2.hexdigest()}')
else:
    print('Arquivos exatamente iguais')
