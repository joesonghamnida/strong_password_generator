import password.password_generation_algorithm
import password.prev_password_checker
from file_handling import file_writer
from file_handling import file_reader

print("Random strong password generator.")

generated_password = password.password_generation_algorithm.generate_password()

print(generated_password)

file_writer.write_to_file(generated_password)
file_reader.read_from_file()

password.prev_password_checker.do_passwords_match(generated_password)
