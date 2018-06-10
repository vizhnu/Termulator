import shutil

def cp(q):
    if len(q) != 3 :
        print("Invalid number of arguments : usage 'cp source dest'")
    else:
        src = q[1]
        dest = q[2]
        try:
            shutil.copyfile(src, dest)
        except FileNotFoundError :
            print("No such file or directory : "+src)
