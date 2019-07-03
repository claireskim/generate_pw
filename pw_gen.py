# Basic password generator, no prompt

import random

pool = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&?"
passlen = 9

gen_pw = F"Your password is {''.join(random.sample(pool,passlen))}"

print(gen_pw)
