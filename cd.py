import os
import re

# I tried to implement this using the os.system('cd path') method but it failed with exit status 0

def cd(q) :
    if len(q) == 1:                     # if user inputs only cd go to root directory
        curdir = os.getcwd()
        root = curdir[:3]               # takes the first three letters which will be the parent directory
        os.chdir(root)                  # cd into root
    elif len(q) == 2:
        dest_dir = q[1]                 # destination directory to cd into
        regobj = re.compile(r'''^[CDEFGH]:\\''')
        # create a regex object to check if the argument to cd command is an absolute path or not
        # mo is a list containing a singel object which is the root directory of argument (if q[1] starts with any letter [CDEFGH])

        mo = regobj.findall(dest_dir)
        if len(mo) == 0:     # path is relative
            par_dir = os.getcwd()
            dest_dir = par_dir+os.sep+dest_dir
        try:
            os.chdir(dest_dir)
        except FileNotFoundError:
            print(dest_dir+"  directory doesn't exist")
        except OSError:
            print(dest_dir+" does not exist")
    else:
        print("too many argumnets; usage: cd path")

