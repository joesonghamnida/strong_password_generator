def write_to_file(password):
    path = '/Users/joe/programming/python/new/password_generator/prev_passwords.txt'

    file = open(path, 'a')
    #TODO: will need to encrypt file contents
    file.write(password + '\n')
    file.close()
