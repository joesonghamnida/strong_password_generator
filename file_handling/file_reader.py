def read_from_file():

    passwords = []
    path = '/Users/joe/programming/python/new/password_generator/prev_passwords.txt'

    file = open(path, 'r')
    #TODO: will need to decrypt and check file contents
    i = 0
    while file.readline():
        passwords.append(file.readline())
    file.close()

    return passwords