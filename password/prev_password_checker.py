from file_handling import file_reader


def do_passwords_match(password):
    passwords = file_reader.read_from_file()

    for str in passwords:
        if str == password:
            print("Previously used password found. Please rerun the program")
