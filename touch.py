def touch(q):
    if len(q) != 2:
        print("invalid number of arguments : usage 'touch filename'")
    else:
        file = q[1]
        try:
            fp = open(file, 'r')
            fp.close()
        except FileNotFoundError:
            fp = open(file, 'w')
            fp.close()
