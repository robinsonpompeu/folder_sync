from pathlib import Path
from shutil import rmtree

folder = Path.cwd() / Path('folder')
rmtree(folder)