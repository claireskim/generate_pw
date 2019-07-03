import random

pool = "abcdefghijklmnopqrstuvwxyz1234567890!?"
passlen = 9

gen_pw = F"Your password is {random.sample(pool,passlen)}."

print gen_pw
