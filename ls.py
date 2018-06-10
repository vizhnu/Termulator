import os


def ls():
    list = os.listdir()
    t_size = os.get_terminal_size()
    width = t_size[0]

    long_list = '\t'.join(list)
    # TODO:print folder names such that a single name does not span more than one lines
    n = width
    if len(long_list) > width:     # unsuccessful effort to prevent folder names from spanning two lines
        while long_list[n] != ' ':
            n -= 1
    print(long_list[:n])
    print(long_list[n:])
