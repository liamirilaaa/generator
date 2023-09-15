import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input('Какой длины должен быть пароль?'))
password = ''

#password generation
for _i in range (length):
  password += random.choice(symbols)
  
print('Ваш пароль', password)
