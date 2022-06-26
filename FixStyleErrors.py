import tkinter.messagebox
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import os
import re


def get_file_name():
    Tk().withdraw()
    filename = askopenfilename()
    if not filename:
        tkinter.messagebox.showerror(title=None, message="No file picked, exiting")
        quit()
    if (os.path.splitext(filename))[1] != ".txt":
        tkinter.messagebox.showerror(title=None, message="Did not pick a .txt file, exiting")
        quit()
    return filename


def format_file():
    searchfilename = get_file_name()
    formattedfilename = (os.path.splitext(searchfilename))[0] + "Formatted" + ".txt"
    formattedfile = open(formattedfilename, 'w')
    searchfile = open(searchfilename, 'r')
    for line in searchfile:
        formattedline = regex_style_line(line.rstrip())
        formattedfile.write(formattedline + "\n")
    searchfile.close()
    formattedfile.close()


def regex_style_line(line):
    # fix arrows
    line = re.sub("->", "â†’", line)

    # fix bullet spacing issues
    if re.match("(?: {0,7}| {9,})-|(?: {0,3}| {5,})â€¢| +â¬¥", line):
        line = re.sub("(?: {0,7}| {9,})-", "        -", line)
        line = re.sub("(?: {0,3}| {5,})â€¢", "    â€¢", line)
        line = re.sub(" +â¬¥", "â¬¥", line)

    # fix emoji spacing issues
    line = re.sub("><", "> <", line)

    # fix missing space before/after emoji issues
    line = re.sub(r"(/|[a-qt-zA-Z0-9]|-|(?:â€¢)|(?:â¬¥)|(?:â†’))<", r"\g<1> <", line)
    line = re.sub(r">(/|[a-qt-zA-Z0-9]|-|(?:â€¢)|(?:â¬¥)|(?:â†’))", r"> \g<1>", line)
    
    # correct the pre- prefix getting a space added
    line = re.sub("pre- <", "pre-<", line)

    return line


if __name__ == '__main__':
    format_file()
