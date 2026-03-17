#1
from app.io.input import input_text_from_console


def output_text_to_console():
    """
    Outputs text to the console

    Args:
    text (str): The text to be displayed in the console
    """
    print(input_text_from_console())
#2
def write_to_file(fileout="output.txt", file="file.txt"):
    """
    Reads content from one file and writes it to another file using built-in Python methods

    Args:
    fileout (str): The name of the file to write to
    file (str): The name of the file to read from
    """
    with open(file, "r") as infile:
        content = infile.read()
    with open(fileout, "w") as outfile:
        outfile.write(content)