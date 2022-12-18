import random
import time
pessoas = [
 'Raissa (indicou Guilherme)',
 'Bruna (indicou Yanca) (A)',
 'Bruna (indicou Elizeth) (A)',
 'Simone (indicou Marcelo) (A)',
 'Renato (indicou Nayara)',
 'Gabi VB (indicou Nayara) (A)',
 'Lairton (indicou Ana Claudia)',
 'Lairton (indicou Matheus)',
 'Lairton (indicou Isabela)',
 'Ariane (indicou Carina) (A)',
 'Matheus (indicou Vaneide)',
 'Lucas (indicou Elizier) (A)',
 'Ingred (indicou Cleber)',
 'Acassio (indicou Marcelo)',
 'Leticia (indicou Juliana)',
 'Joyce (indicou Juliana)',
 'Joyce (indicou Matheus)',
 'Nat Gomes (indicou Jaqueline)' ]
print('\n\n\n\nvamos começar?\n\n\n')
time.sleep(2)
print('se prepare!\n\n\n')
time.sleep(2)
print('...sorteando...\n\n\n')
time.sleep(2)
print(f'\n\n\n\n O ganhador foi: \n\n\n  {pessoas [ random.randrange ( len ( pessoas ))]} \n\n\n\n\n\n')