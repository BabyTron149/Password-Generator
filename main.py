from random import choice


password = ""
simbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
col = int(input("Из скольки символов должен состоять пароль? "))
if col < 8:
    print("не подходит по стандарту, был сгенерирован пароль из 8 символов")
    col = 8
for index in range(col):
    password += choice(simbols)
print(password)
