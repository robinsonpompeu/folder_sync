"""
Background user-driven folder modifications

Simulates user interactions by creating, modifying and deleting files and 
folders at random in scheduled intervals. It performs the following steps:
- Parses command line arguments passed by main.py
- Configures the log process with fixed log filepath
- Executes random operations on source or replica folders

By default it performs 20 operations every 5 seconds.

Arguments:
-----
    --source_dir      Absolute path of source dir
    --replica_dir     Absolute path of replica dir
    --log_file        Absolute path of bot log file
    --t_interval      Time interval in seconds between operations

Notes:
-----
    - The user running this script must have write permissions on both folders
    - Source and replica absolute paths must have a trailing slash
    - Only one big file (aroung 1GB) will be created in each simulation.
"""

import argparse
import os
import subprocess
import sys
import time

import numpy as np
import pandas as pd

from random import choice, choices
from pathlib import Path
from shutil import rmtree

parser = argparse.ArgumentParser(description = 'Bot user configuration.')
parser.add_argument(
    '--source_dir', 
    type = str,
    required = True, 
    help = 'Absolute path of source directory.'
)
parser.add_argument(
    '--replica_dir', 
    type = str,
    required = True, 
    help = 'Absolute path of replica directory.'
)
parser.add_argument(
    '--log_file', 
    type = str,
    required = True, 
    help = 'Absolute path of log file.'
)
parser.add_argument(
    '--t_interval', 
    type = float, 
    help = 'Synchronization interval.'
)

args = parser.parse_args()

N_ELEM = 5
N_OPER = 20

dir_list = [args.source_dir, args.replica_dir]
name_list = ['foo', 'bar', 'baz', 'qux']
ext_list = ['.txt']

def create_dir(sub_dir, **kwargs):
    name_list = kwargs['name_list']
    n_elem = kwargs['n_elem']
    folder_name = f"{choice(name_list)}{choice(range(1, n_elem + 1))}"
    make_dir = Path(sub_dir) / Path(folder_name)
    make_dir.mkdir(parents = True, exist_ok = True)
    return f"\nBOT created {str(make_dir)}."

def remove_dir(sub_dir, **kwargs):
    source_dir = kwargs['source_dir']
    print(str(sub_dir))
    print(str(source_dir))
    if str(sub_dir) + '/' != source_dir:
        rmtree(Path(sub_dir))
        return f"\nBOT removed {str(sub_dir)}."
    else:
        return f"\nDir {str(sub_dir)} cannot be removed."

def create_file(sub_dir, **kwargs):
    name_list = kwargs['name_list']
    n_elem = kwargs['n_elem']
    file_name = f"{choice(name_list)}{choice(range(1, n_elem))}.txt"
    file = Path(sub_dir) / Path(file_name)
    if not Path(sub_dir).exists():
        Path(sub_dir).mkdir(parents = True)
    file.touch()
    return f"\nBOT created {str(file)}."
    
def create_big_file(sub_dir, **kwargs):
    ROWS = 3_000_000
    COLS = 100
    df_big = np.ones([ROWS, COLS])
    path = Path(sub_dir) / Path('big_file.csv')
    pd.DataFrame(df_big).to_csv(str(path))
    del df_big
    return f"BOT created a big file at {str(path)}.", str(path)

def modify_file(sub_dir, **kwargs):
    file_name = kwargs['file_name']
    file = Path(sub_dir) / Path(file_name)
    content = ''.join([choice(range(1, 101)) for n in range(1, 101)])
    with file.open("a") as f:
        f.write(content)
    return f"\nBOT edited {str(file)}."

def delete_file(sub_dir, **kwargs):
    file_name = kwargs['file_name']
    file = Path(sub_dir) / Path(file_name)
    file.unlink()
    return f"\nBOT removed {str(file)}."
    
if __name__ == '__main__':
    
    # Decorates all functions for logging
    import folder_sync.log_recorder as log_recorder
    log_recorder.decorate(sys.modules[__name__], log_recorder.log, args.log_file)
    
    oper_list = [create_dir, remove_dir, create_file, modify_file, delete_file]
    big_file = False
    for n in range(N_OPER):
        # Choose to modify source or replica dirs
        dir_oper = choice(dir_list)
        
        # Choose a subfolder to modify or create a new one if empty
        sub_dir_list = [dirs for dirs, _, _, in Path(dir_oper).walk()]
        if sub_dir_list == []:
            sub_dir = Path(dir_oper) / Path(choice(name_list))
            sub_dir.mkdir(parents = True, exist_ok = True)
        else:
            sub_dir = Path(choice(sub_dir_list))
        
        # Decide whether or not to create a big file if it doesn't exist
        if big_file == False and choice([True, False]) == True:
            msg, big_file_path = create_big_file(str(sub_dir))
            print(msg)
            big_file = True
        else:
            # Choose a random folder modification
            oper = choices(oper_list, weights = (30, 5, 35, 15, 15))[0]
            
            # Specify a file to be modified or deleted
            if oper in  [modify_file, delete_file]:
                file_list = [f for f in Path(sub_dir).iterdir() if f.is_file()]
                if file_list == []:
                    # Create a foo1.txt file if folder is empty
                    create_file(str(sub_dir), **{'name_list': ['foo'], 'n_elem': 2})
                    file_name = 'foo1.txt'
                else:
                    file_name = choice(file_list)
                    
            # Attempt to modify folder
            try:
                print(oper(str(sub_dir), **{
                           'name_list': name_list, 
                           'n_elem': N_ELEM, 
                           'source_dir': args.source_dir,
                           'file_name': file_name
                           }
                     )
                )
            except Exception as e:
                pass
        time.sleep(args.t_interval)
    print("\nBOT finished simulation.")