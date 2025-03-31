import pytest
import numpy as np

from pathlib import Path
from subprocess import Popen

from vol_manager import remove_file, remove_dir, update_dest

@pytest.mark.parametrize("file_path", [None, True, False, 0, 1.0, b"file.txt"])
def test_remove_file_invalid_input(file_path):
    with pytest.raises(TypeError) as excinfo:
        remove_file(file_path)
    assert str(excinfo.value) == "File path is not a valid string."

def test_remove_file_existent_file(existent_file):
    remove_file(existent_file)
    assert Path(existent_file).exists() == False

def test_remove_file_nonexistent_file(nonexistent_file):
    with pytest.raises(FileNotFoundError) as excinfo:
        remove_file(nonexistent_file)
    assert str(excinfo.value) == f"File {str(nonexistent_file)} not found."

def test_remove_file_without_permission_file(without_permission_file):
    with pytest.raises(PermissionError) as excinfo:
        remove_file(without_permission_file)
    assert str(excinfo.value) == f"Permission denied to remove {str(without_permission_file)}."

@pytest.mark.parametrize("dir_path", [None, True, False, 0, 1.0, b"file.txt"])
def test_remove_dir_invalid_input(dir_path):
    with pytest.raises(TypeError) as excinfo:
        remove_dir(dir_path)
    assert str(excinfo.value) == "Folder path is not a valid string."

def test_remove_dir_empty_dir(empty_dir):
    remove_dir(empty_dir)
    assert Path(empty_dir).exists() == False

def test_remove_dir_existent_dir(existent_dir):
    remove_dir(existent_dir)
    assert Path(existent_dir).exists() == False

def test_remove_dir_existent_dir(existent_dir):
    remove_dir(existent_dir)
    assert Path(existent_dir).exists() == False

def test_remove_dir_nonexistent_dir(nonexistent_dir):
    with pytest.raises(FileNotFoundError) as excinfo:
        remove_dir(nonexistent_dir)
    assert str(excinfo.value) == f"Folder path {str(nonexistent_dir)} not found."

def test_remove_dir_without_permission(without_permission_dir):
    with pytest.raises(PermissionError) as excinfo:
        remove_dir(without_permission_dir)
    assert str(excinfo.value) == f"Permission denied to remove {str(without_permission_dir)}."

@pytest.mark.parametrize("source_path", [None, True, False, 0, 1.0, b"file.txt"])
@pytest.mark.parametrize("replica_path", ['folder/update_replica/file.txt'])
def test_update_dest_source_invalid_input(source_path, replica_path):
    with pytest.raises(TypeError) as excinfo:
        update_dest(source_path, replica_path)
    assert str(excinfo.value) == "Source path is not a valid string."

@pytest.mark.parametrize("source_path", ['folder/update_source/file.txt'])
@pytest.mark.parametrize("replica_path", [None, True, False, 0, 1.0, b"file.txt"])
def test_update_dest_replica_invalid_input(source_path, replica_path):
    with pytest.raises(TypeError) as excinfo:
        update_dest(source_path, replica_path)
    assert str(excinfo.value) == "Replica path is not a valid string."

def test_update_dest_nonexistent_replica_file(source_existent_file, replica_nonexistent_file):
    update_dest(source_existent_file, replica_nonexistent_file)
    assert Path(replica_nonexistent_file).exists() == True

def test_update_dest_nonexistent_source_file(source_nonexistent_file, replica_nonexistent_file):
    with pytest.raises(Exception) as excinfo:
        update_dest(source_nonexistent_file, replica_nonexistent_file)
    assert str(excinfo.value) == "Source path is not valid."

def test_update_dest_existent_replica_file(source_existent_file, replica_existent_file):
    update_dest(source_existent_file, replica_existent_file)
    assert Path(replica_existent_file).exists() == True

def test_update_dest_source_file_without_permission(without_permission_source_file, replica_existent_file):
    with pytest.raises(PermissionError) as excinfo:
        update_dest(without_permission_source_file, replica_existent_file)
    assert str(excinfo.value) == f"[Errno 13] Permission denied: '{str(without_permission_source_file)}'"