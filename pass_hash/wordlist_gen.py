import itertools

string_to_permute = input('Digite o texto a ser permutado: ')

result = itertools.permutations(string_to_permute, len(string_to_permute))

for char in result:
    print(''.join(char))