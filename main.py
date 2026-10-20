import random

class small_password():
    pass

def passwordGenerator(bit):
    character = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!£$%&/()=?^É*§°Ç;:_-.,ÙÀÒ+ÈÌ"
    password = ""

    for x in range(bit):
        if bit < 5:
            raise small_password("La password è troppo piccola")
        car = random.choice(character)
        password+=car
    return password

print(passwordGenerator(10))

