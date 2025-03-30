"""
Volume Manager Operations

This module implements operations required to ensure folder synchronization.
For the sake of clarity only one update replica method is implemented (rather 
than file and dir copy methods), since some files in a given parent folder may
not require to be updated if the parent folder is modified.

Notes
-----
    With respect to error handling the approach used here is based on EAFP 
    Python principle (which states that it is "easier to ask forgiveness 
    than permission").
    
    Exception handling is focused on folder and file accessibility and permission
    policies. Other exceptions are handled in such a way that their details
    are logged for further inspection.

"""

from pathlib import Path
from shutil import rmtree, copy2

def remove_file(file_path):
    """
    Attempt to remove a file given its location.
    
    Parameters
    ----------
    file_path : str
        Absolute filepath of file to be removed.
    
    Returns
    -------
    str
        File path if successfully removed.
    
    Raises
    ------
    TypeError
        File path provided is not a valid string.
    FileNotFoundError
        File path associated with a nonexisting file.
    PermissionError
        File without necessary permissions to be deleted.
    Exception
        Any other error raised.
    """
    if not isinstance(file_path, str):
        raise TypeError("File path is not a valid string.")
    file = Path(file_path)
    try:
        file.unlink()
        return str(file)
    except FileNotFoundError:
        raise FileNotFoundError(f"File {str(file)} not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to remove {str(file)}.")
    except Exception as err:
        raise err(f"Unexpected {err=}, {type(err)=}")

def remove_dir(dir_path):
    """
    Attempt to remove a folder given its location.
    
    Parameters
    ----------
    dir_path : str
        Absolute path of folder to be removed.
    
    Returns
    -------
    str
        Folder path if successfully removed.
    
    Raises
    ------
    FileNotFoundError
        Folder path associated with a nonexisting dir.
    PermissionError
        Folder without necessary permissions to be deleted.
    Exception
        Any other error raised.
    
    """
    if not isinstance(dir_path, str):
        raise TypeError("Folder path is not a valid string.")
    folder = Path(dir_path)
    try:
        rmtree(folder)
        return str(folder)
    except FileNotFoundError:
        raise FileNotFoundError(f"Folder path {str(folder)} not found.")
    except PermissionError:
        raise PermissionError(f"Permission denied to remove {str(folder)}.")
    except Exception as err:
        raise err(f"Unexpected {err=}, {type(err)=}")

def update_dest(source_path, replica_path):
    """
    Duplicate replica folder structure with items not synchronized from source.
    
    Creates the corresponding replica folder in case `source_path` points to a 
    folder not present in replica, or copies to replica the source file indicated
    in `source_path`.
    
    Parameters
    ----------
    source_path : str
        Absolute folder or file path from source dir.
    replica_path : str
        Absolute folder or file path on replica dir
    
    Returns
    -------
    str
        Absolute path of updated file or folder on replica dir.
    
    Raises
    ------
    TypeError
        Folder or file path provided is not a valid string.
    Exception
        Any other error raised.
    """
    if not isinstance(source_path, str):
        raise TypeError("Source path is not a valid string.")
    source = Path(source_path)
    if not isinstance(replica_path, str):
        raise TypeError("Replica path is not a valid string.")
    replica = Path(replica_path)
    if source.is_dir():
        if not replica.exists():
            try:
                replica.mkdir(parents = True)
                return str(replica)
            except Exception as err:
                raise err(f"Unexpected {err=}, {type(err)=}")
    elif source.is_file():
        try:
            copy2(source, replica)
            return str(replica)
        except PermissionError:
            raise PermissionError(f"Without write permission.")
        except OSError:
            raise OSError(f"OS Error occured. Check disk usage.")
        except Exception as err:
            raise err(f"Unexpected {err=}, {type(err)=}")
    else:
        raise Exception("Source path is not valid.")