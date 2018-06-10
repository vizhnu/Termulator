import  shutil
def mv(q):
    if len(q) != 3:
        print("Invalid numer of arguments : usage 'mv source dest'")
    else:
        src = q[1]
        dest = q[2]
        try:
            shutil.move(src,dest)
        except FileNotFoundError:
            print("No such file or directory : "+dest)
