import os
import nbformat
from nbformat.v4 import new_notebook, new_code_cell

def convert_py_to_ipynb(py_file_path):
    # Determine the output path
    ipynb_file_path = py_file_path.replace('.py', '.ipynb')
    
    # Read the python file
    with open(py_file_path, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # Create a new notebook
    nb = new_notebook()
    
    # Add a single cell with all the code
    nb.cells.append(new_code_cell(code))
    
    # Write the notebook
    with open(ipynb_file_path, 'w', encoding='utf-8') as f:
        nbformat.write(nb, f)
    
    print(f"Converted {py_file_path} -> {ipynb_file_path}")

# Directory path
dir_path = 'C:/Users/ADMIN/Desktop/Bike_Sharing_Project'

# List all .py files
py_files = [f for f in os.listdir(dir_path) if f.endswith('.py')]

for f in py_files:
    convert_py_to_ipynb(os.path.join(dir_path, f))

print("\nAll conversions completed.")
