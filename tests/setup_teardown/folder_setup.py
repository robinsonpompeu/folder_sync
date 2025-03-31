import pandas as pd
import numpy as np

from pathlib import Path
from shutil import rmtree

SMALL_CONTENT = 'Small content.'

folder_list = [
    'folder/empty',
    'folder/remove_file/without_permission',
    'folder/remove_dir/parent',
    'folder/remove_dir_without_permission/parent',
    'folder/update_source/without_permission',
    'folder/update_replica/without_permission'
]
for folder in folder_list:
    (Path.cwd() / Path(folder)).mkdir(parents = True)

file_list = [
    'folder/remove_file/file.txt',
    'folder/remove_file/file_in_use.txt',
    'folder/remove_file/without_permission/file.txt',
    'folder/remove_dir/file.txt',
    'folder/remove_dir/parent/file.txt',
    'folder/remove_dir_without_permission/file.txt',
    'folder/remove_dir_without_permission/parent/file.txt',
    'folder/update_source/file.txt',
    'folder/update_replica/file.txt',
    'folder/update_source/without_permission/file.txt',
    'folder/update_replica/without_permission/file.txt'
]
for file in file_list:
    filepath = Path.cwd() / Path(file)
    with filepath.open("w", encoding = "utf-8") as f:
        f.write(SMALL_CONTENT)

(Path.cwd() / Path('folder/remove_file/without_permission')).chmod(0o000)
(Path.cwd() / Path('folder/remove_dir_without_permission')).chmod(0o000)
(Path.cwd() / Path('folder/update_source/without_permission')).chmod(0o000)
(Path.cwd() / Path('folder/update_replica/without_permission')).chmod(0o000)