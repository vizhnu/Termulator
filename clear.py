import os

#  clears the screen, but the new prompt is at the end of the window, need to fix that
def clear():
    size_data = os.get_terminal_size()  # returns a tuple (columns, rows)
    rows = size_data[1]  # gets the no of rows and prints newlines
    for i in range(rows):
        print()
