# Termulator , a linux terminal emulator for windows
# options are not supported yet
import os
import pwd
import ls
import clear
import cd
import cp
import mv
import touch

# TODO: mkdir, rm, cat, echo, maybe pipes :/


print("          Termulator")
if os.name != 'nt':
    print("You are not using Windows.Termulator is for Windows systems only")
    exit(1)
user = os.getlogin()
while 1:
    try:
        q = input(user + '$')
        q = q.split()
        print(q)
    except KeyboardInterrupt:
        exit(1)
    try:
        if q[0] == 'pwd':
            pwd.pwd()
        elif q[0] == "ls":
            ls.ls()
        elif q[0] == "clear":
            clear.clear()
        elif q[0] == "cd":
            cd.cd(q)
        elif q[0] == "cp":
            cp.cp(q)
        elif q[0] == "mv":
            mv.mv(q)
        elif q[0] == "touch":
            touch.touch(q)
        else:
            print(q[0] + " is not a recognizable command")  # default
    except IndexError:
        continue
