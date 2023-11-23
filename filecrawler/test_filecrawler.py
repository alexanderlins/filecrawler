import pytest
import os


# Tests that the application starts by receiving a string
def test_receiving_a_string():
    string = "Kött"
    assert type(string) == str


# Tests if the current directory is a directory.
def test_current_directory():  
    current_directory = os.path.dirname(os.path.realpath(__file__))
    assert os.path.isdir(current_directory)


# Tests if there are other folders in directory
def test_contents_in_directory():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = "TestData"
    test_data_path = os.path.join(current_directory, path)
    assert os.path.exists(test_data_path)
    

# Tests if we can access other folders within another folder.
def test_another_path_in_directory():
    current_directory = os.path.dirname(os.path.realpath(__file__))
    path = "TestData"
    test_data_path = os.path.join(current_directory,path)
    another_path = "Drycker"
    test_another_path = os.path.join(test_data_path, another_path)
    assert os.path.exists(test_another_path)
