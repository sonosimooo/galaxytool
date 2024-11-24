import os
import time
import shutil
import chardet
from fpdf import FPDF
from pystyle import Write, Colors

# Path configuration
input_folder = os.path.join("data", "input")
output_folder = os.path.join("data", "output")


def print_title():
    """Prints the application title."""
    Write.Print(r'''
 _______  _______  ______   ___ ___  _______  _______  _______    _______  ___  ___      _______ 
|   _   ||   _   ||   _  \ |   Y   ||   _   ||   _   \|       |  |   _   ||   ||   |    |   _   |
|.  1___||.  |   ||.  |   ||.  |   ||.  1___||.  l   /|.|   | |  |.  1___||.  ||.  |    |.  1___|
|.  |___ |.  |   ||.  |   ||.  |   ||.  __)_ |.  _   1`-|.  |-'  |.  __)  |.  ||.  |___ |.  __)_ 
|:  1   ||:  1   ||:  |   ||:  1   ||:  1   ||:  |   |  |:  |    |:  |    |:  ||:  1   ||:  1   |
|::.. . ||::.. . ||::.|   | \:.. ./ |::.. . ||::.|:. |  |::.|    |::.|    |::.||::.. . ||::.. . |
`-------'`-------'`--- ---'  `---'  `-------'`--- ---'  `---'    `---'    `---'`-------'`-------'
                                                                                                 
                                                                               
    ''', Colors.black_to_red, interval=0.001)


def print_menu():
    """Prints the application menu."""
    Write.Print(r'''
    ---------- FILE TOOLS MENU ---------- 
          1- FILE TO PDF
          0- EXIT
    -------------------------------------
''', Colors.black_to_red)


def detect_file_encoding(file_path):
    """Detects the encoding of a file."""
    with open(file_path, 'rb') as file:
        raw_data = file.read()
        result = chardet.detect(raw_data)
        return result['encoding']


def clear_folder(folder):
    """Clears all files in the given folder."""
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def get_single_file_from_folder(folder):
    """Gets the single file from a folder."""
    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
    if len(files) != 1:
        Write.Print(f"Error: The folder '{folder}' must contain exactly one file.\n", Colors.red_to_black)
        return None
    return os.path.join(folder, files[0])


def convert_to_pdf(input_file, output_file):
    """Converts a text file to a PDF."""
    try:
        encoding = detect_file_encoding(input_file)
        Write.Print(f"Detected encoding: {encoding}\n", Colors.white_to_green)

        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        with open(input_file, 'r', encoding=encoding) as file:
            for line in file:
                pdf.cell(200, 10, txt=line.strip(), ln=True)

        pdf.output(output_file)
        Write.Print(f"File successfully converted and saved to: '{output_file}'\n", Colors.white_to_green)

    except UnicodeDecodeError:
        Write.Print(f"Error: Unable to decode the file. Try checking the file's encoding.\n", Colors.red_to_black)
    except Exception as e:
        Write.Print(f"Error during conversion: {e}\n", Colors.red_to_black)


def main_menu():
    """Displays the main menu and handles user input."""
    while True:
        os.system("cls")
        print_title()
        print_menu()

        Write.Print(">> ", Colors.black_to_red)
        choice = input().strip()

        if choice == "1":
            file_path = get_single_file_from_folder(input_folder)
            if file_path is None:
                input("\nPress Enter to return to the menu...")
                continue

            base_name = os.path.splitext(os.path.basename(file_path))[0]
            output_file = os.path.join(output_folder, f"{base_name}.pdf")
            convert_to_pdf(file_path, output_file)

            input("\nPress Enter to return to the menu...")
        elif choice == "0":
            Write.Print("Exiting the tool. Goodbye!\n", Colors.black_to_red)
            break
        else:
            Write.Print("Invalid option. Please try again.\n", Colors.red_to_black)
            time.sleep(1)


if __name__ == "__main__":
    # Ensure the input and output folders exist
    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)

    main_menu()
