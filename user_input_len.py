# User prompted number of characters and generate a random password

import string as s
import random

def pass_gen(size=20, p=s.ascii_letters + s.digits + s.punctuation):
  return ''.join(random.choice(p) for _ in range(size))
  
print(pass_gen(int(input("Generate a password: how many characters?"))))
