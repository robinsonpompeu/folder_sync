import pytest

from pathlib import Path

@pytest.fixture
def existent_file():
    test_path = Path.cwd() / Path('folder/remove_file')
    test_file = 'file.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def nonexistent_file():
    test_path = Path.cwd() / Path('folder/remove_file')
    test_file = 'nonexistent_file.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def without_permission_file():
    test_path = Path.cwd() / Path('folder/remove_file/without_permission')
    test_file = 'file.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def file_in_use():
    test_path = Path.cwd() / Path('folder/remove_file')
    test_file = 'file_in_use.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def empty_dir():
    test_path = Path.cwd() / Path('folder/empty')
    return str(test_path)
    
@pytest.fixture
def existent_dir():
    test_path = Path.cwd() / Path('folder/remove_dir')
    return str(test_path)

@pytest.fixture
def nonexistent_dir():
    test_path = Path.cwd() / Path('folder/nonexistent_dir')
    return str(test_path)

@pytest.fixture
def without_permission_dir():
    test_path = Path.cwd() / Path('folder/remove_dir_without_permission')
    return str(test_path)

@pytest.fixture
def source_existent_dir():
    test_path = Path.cwd() / Path('folder/update_source/file.txt')
    return str(test_path)

@pytest.fixture
def replica_existent_dir():
    test_path = Path.cwd() / Path('folder/update_replica/file.txt')
    return str(test_path)

@pytest.fixture
def source_existent_file():
    test_path = Path.cwd() / Path('folder/update_source')
    test_file = 'file.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def source_nonexistent_file():
    test_path = Path.cwd() / Path('folder/update_source')
    test_file = 'nonexistent_file.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def replica_existent_file():
    test_path = Path.cwd() / Path('folder/update_replica')
    test_file = 'file.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def replica_nonexistent_file():
    test_path = Path.cwd() / Path('folder/update_replica')
    test_file = 'nonexistent_file.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def without_permission_source_dir():
    test_path = Path.cwd() / Path('folder/update_source/without_permission')
    return str(test_path)

@pytest.fixture
def without_permission_source_file():
    test_path = Path.cwd() / Path('folder/update_source/without_permission')
    test_file = 'file.txt'
    return str(Path(test_path) / Path(test_file))

@pytest.fixture
def without_permission_replica_dir():
    test_path = Path.cwd() / Path('folder/update_replica/without_permission')
    return str(test_path)

@pytest.fixture
def without_permission_replica_file():
    test_path = Path.cwd() / Path('folder/update_replica/without_permission')
    test_file = 'file.txt'
    return str(Path(test_path) / Path(test_file))