#!/usr/bin/env python3

import string
from random import choice, randint
from time import sleep

x = input('PW Mnemonic ID: ')

path = './.later_retrieval.log' # Plan text log in home directory, set as a hidden dot file.
later = open(path, 'a')

characters = string.ascii_letters + string.digits + string.punctuation
p = "".join(choice(characters)for x in range(randint(32, 32))) # Number of charactors long.

print(p)
later.write('\n' + x + ': ' + (p))
later.close()
sleep(10)
