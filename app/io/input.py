import pandas as pd

#1
def input_text_from_console():
    """
    Ask user to write text in the console
    This function reads a line of text input from the user

    Args:
    user_input (str): Content that was written by user

    Returns:
    str: The content of writing
    """
    user_input = input("Please enter some text: ")
    return user_input
#2
def read_file():
    """
    Reads content from a file using built-in Python methods
    This function takes the file name as an argument and returns its content

    Args:
    filename (str): The name of the file to be read

    Returns:
    str: The content of the file
    """
    with open(file, "r") as file:
        content = file.read()
    return content
#3
def read_file_pandas():
    """
    Reads content from a file using the pandas library
    This function loads a file into a pandas DataFrame

    Args:
    filename (str): The name of the file to be read

    Returns:
    pandas.DataFrame: The data from the file
    """
    data = pd.read_csv(file)
    return data
