# filename: install_matplotlib.py
import subprocess
import sys

# Function to install a package using pip
def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

# Install matplotlib
install('matplotlib')