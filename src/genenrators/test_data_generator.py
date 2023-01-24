import random
import string


# генерим рандомную строку
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_random_email(length):
    email_name = generate_random_string(length)
    return email_name + '@test.ru'

