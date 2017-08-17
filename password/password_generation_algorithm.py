import random

characters = 'abcdefghijklmnopqrstuvwxyz'

numbers = '1234567890'

symbols = '!@#$%^&*()_+-='


def is_letter_uppercase(letter):
    number = random.randint(0, 1)
    if number == 0:
        letter = letter.upper()
    return letter


# TODO: will need to make this stuff truly random. Should also include options to not use illegal chars
def generate_password():
    new_password = ""

    i = 0
    while i < 24:
        character_set_selector = random.randrange(0, 3)

        if character_set_selector == 0:
            letter = characters[random.randint(0, 25)]
            letter = is_letter_uppercase(letter)
            new_password = new_password + letter
        elif character_set_selector == 1:
            new_password = new_password + numbers[random.randint(0, 9)]
        else:
            new_password = new_password + symbols[random.randint(0, 13)]
        i = i + 1

    return new_password
