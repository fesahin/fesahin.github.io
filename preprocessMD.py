import os
import shutil
import argparse

def replace_text_in_md(input_dir, replacements, output_dir):
    """
    Replaces text in .md files within a directory and saves the modified files
    to a new directory. Also copies all other files and directories.

    Args:
        input_dir (str): The path to the input directory.
        replacements (dict): A dictionary of text replacements (old_text: new_text).
        output_dir (str): The path to the output directory.
    """

    os.makedirs(output_dir, exist_ok=True)

    for item in os.listdir(input_dir):
        input_item_path = os.path.join(input_dir, item)
        output_item_path = os.path.join(output_dir, item)

        if os.path.isfile(input_item_path):
            if input_item_path.lower().endswith(".md"):
                with open(input_item_path, "r", encoding="utf-8") as f:
                    content = f.read()

                for old_text, new_text in replacements.items():
                    content = content.replace(old_text, new_text)

                with open(output_item_path, "w", encoding="utf-8") as f:
                    f.write(content)
            else:
                shutil.copy2(input_item_path, output_item_path)

        elif os.path.isdir(input_item_path):
            shutil.copytree(input_item_path, output_item_path, dirs_exist_ok=True)


def main():
    """
    Main function to parse command-line arguments and run the text replacement.
    """
    parser = argparse.ArgumentParser(description="Replace text in .md files.")
    parser.add_argument("input_dir", help="The input directory containing .md files.")
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = os.path.join(input_dir, "_output")

    # Define the replacements as a dictionary.
    replacements = {
        "%%hs": "[hiddennote]: # (",
        "he%%": ")",
    }


    replace_text_in_md(input_dir, replacements, output_dir)
    print(f"Text replacement completed. Output saved to: {output_dir}")

if __name__ == "__main__":
    main()