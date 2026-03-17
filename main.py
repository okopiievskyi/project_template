from app.io.input import input_text_from_console, read_file, read_file_pandas
from app.io.output import output_text_to_console, write_to_file

def main():
    user_input = input_text_from_console()
    output_text_to_console(f"You entered: {user_input}")

    content = read_file("file.txt")
    output_text_to_console(f"\nFile content: {content}")

    data = read_file_pandas("file.txt")
    output_text_to_console(f"\nData from CSV file:\n{data}")

    write_to_file("output.txt", "file.txt")

if __name__ == "__main__":
    main()