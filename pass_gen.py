#!/usr/bin/env python3

import string
from random import choice, randint
from time import sleep

x = input('PW Mnemonic id: ')

path = './.later_retrieval.log' # Plan text log in home directory, set as a hidden dot file.
later = open(path, 'a')

ok_punc = '(#!_~)' # Custom list of punctuation.
characters = string.ascii_letters + string.digits + ok_punc
p = "".join(choice(characters)for x in range(randint(16, 16))) # Number of charactors long.

print(p)
later.write('\n' + x + ': ' + (p))
later.close()
sleep(10)
