import os
from pathlib import Path

import subprocess
##download the files / dataset 
url = "http://files.srl.inf.ethz.ch/data/py150_files.tar.gz"
output_filename = "py150_files.tar.gz"

subprocess.run(["wget", "-O", output_filename, url], check=True)

print(f"Downloaded: {output_filename}")    

def collect_python_files(source_dir, output_file):
    """Reads all Python files and writes their content to a single text file."""
    with open(output_file, "w", encoding="utf-8") as outfile:
        for py_file in Path(source_dir).rglob("*.py"):  # Find all Python files
            if py_file.is_file():  # ✅ Check if it's an actual file, not a directory
                with open(py_file, "r", encoding="utf-8", errors="ignore") as infile:
                    outfile.write(infile.read() + "\n\n")  # Separate files by newline

# Specify directory containing Python source files
source_directory = "/home/kifal/assign1/data"  # Adjust to your dataset path
output_corpus = "python_corpus.txt"

collect_python_files(source_directory, output_corpus)
print(f"✅ Combined all Python files into {output_corpus}")
