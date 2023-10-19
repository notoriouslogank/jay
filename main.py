# The first thing you do in any Python module is to import whatever dependancies you have

# Think of the import statements like this: if I created a function I really like and want to reuse in THIS program, I could 
# 'import main' in another program and get access to all of the functions in THIS program.  Does that make sense?  It's like
# we're pulling in other Python scripts into our program so we have access to functions.  They don't all load by default, because
# there are just too many, it'd kill the efficiency.
import random

message = 'You rolled a: ' # Do we need this message saved as a variable?  Will this message ever change?
die = random.randint(1, 20)

print(message, die)
print('You rolled a: ', die)

'''Questions:

1) Add an output for a second die, six-sided this time (so one d20, one d6)

2) Add an output to flip a coin.

3) Can you output all of these things -- 1d20, 1d6, and one coin -- as a single message?
'''