"""
Directory Monitor Module

This module contains two functions that are responsible for a directory
surveillance for modifications.

Notes
-----
    The hash computation of folders was not implemented by a deliberate
    choice at the project planning step. In this first version, folder
    modifications are interpreted solely as file changes, although other
    operations (e.g. access permission alterations) of folders may correspond
    to directory modifications.

"""

import hashlib
import pandas as pd

from pathlib import Path, PurePath

def list_tree(dir):
    """
    Fill a dataframe with dir tree structure.
    
    The dataframe index corresponds to the relative path,
    with respect to `dir`, of all files and folders on dir,
    and hash column stores the computed hash of all files (as
    mentioned in the module description, hash of folders is not
    implemented in the first version of the folder sync project).
    
    Parameters
    ----------
    dir : str
        Absolute path of directory to be monitored.
    
    Returns
    -------
    pandas.Dataframe
        Dataframe with relative paths of folders and files as dataframe
        index, along with the file hashes in hash column.
    
    Raises
    ------
    TypeError
        Dir input is not a valid string path.
    """
    if not isinstance(dir, str) or not Path(dir).is_dir():
        raise TypeError("Dir path is not a valid string path.")
    df = pd.DataFrame(columns = ['path', 'hash'])
    df.set_index('path', inplace = True)
    for dirs, _, files in Path(dir).walk():
        df.loc[str(PurePath(dirs).relative_to(dir))] = {'hash': ''}
        for file in sorted(files):
            filepath = PurePath(dirs).relative_to(dir) / Path(file)
            if not str(filepath) in df.index:
                df.loc[str(filepath)] = {
                    'hash': hash_file(str(Path(dir) / filepath))
                }
    return df

def hash_file(filepath):
    """
    Returns the sha256 hash of a file.
    
    Parameters
    ----------
    filepath : str
        Absolute path of file to compute hash.
    
    Returns
    -------
    str
        String with the hexadecimal hash digest.
    
    Raises
    ------
    Exception
        MUST BE IMPROVED HERE.
    """
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(64 * 128):
            sha256.update(chunk)
    return sha256.hexdigest()