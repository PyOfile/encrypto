#!/usr/bin/env python3

import string
from random import choice, randint
from time import sleep

x = input('PW Mnemonic id: ')

path = './.later_retrieval.log'
later = open(path, 'a')

ok_punc = '(#!_~)'
characters = string.ascii_letters + string.digits + ok_punc
p = "".join(choice(characters)for x in range(randint(16, 16)))

print(p)
later.write('\n' + x + ': ' + (p))
later.close()
sleep(10)

