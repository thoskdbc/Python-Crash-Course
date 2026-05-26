# 8-15. Printing Models: Put the functions for the example printing_models.py in a
# separate file called printing_functions.py. Write an import statement at the top
# of printing_models.py, and modify the file to use the imported functions.
from printing_functions import *
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
print_models(unprinted_designs, completed_models)

# Display all completed models.
show_completed_models(completed_models)



# 8-16. Imports: Using a program you wrote that has one function in it, store that
# function in a separate file. Import the function into your main program file, and
# call the function using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *
import useless
useless.ask("bulk")
from useless import ask
ask("network")
from useless import ask as doubt
doubt("internet")
import useless as ul
ul.ask("data")
from useless import *
ask('time')


# 8-17. Styling Functions: Choose any three programs you wrote for this chapter,
# and make sure they follow the styling guidelines described in this section.
# xd