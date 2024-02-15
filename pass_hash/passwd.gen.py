import random
import string

SIZE = input('Digite o tamanho da senha desejada: ')

CHARS = string.ascii_letters + string.digits + '!@#$%&*()-=+[]\/|'

random_func = random.SystemRandom() #os.urandom

print("".join(random_func.choice(CHARS) for digit in range(int(SIZE))))
