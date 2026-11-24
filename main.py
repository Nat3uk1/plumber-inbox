"""Write the Plumber's Inbox entry text to the make.fun output directory."""

import os
import shutil


def main():
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "text.txt")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(output_dir, "entry.txt"))


if __name__ == "__main__":
    main()
