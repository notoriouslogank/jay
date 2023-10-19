# This is an import statement
import os

# This is a variable declaration
adjective = input('Adjective: ')
noun = input('Noun: ')

# This is a function call.
print(f'That is one {adjective} {noun}!')

# Another variable.  Notice that a variable can be a value, like 'noun', or even a function itself.
current_directory = os.getcwd()

# These functions are equivalent:
print(current_directory)
print(os.getcwd())