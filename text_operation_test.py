 import text_operation

from os.path import exists
import urllib.request
import pytest


def test_task7():
    input = "grzegorz@sda.pl,sara@facebook.com"
    output = "grzegorz,sara"
    assert text_operation.task7(input) == output


def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def test_connection():
    connection = connect()
    assert connection


def check_numpy_library():
    try:
        import os
        return True
    except:
        return False


def test_library():
    assert check_numpy_library()



@pytest.mark.parametrize('file_name', ['sample_file.txt', 'text_operation.py'])
def test_file(file_name):
    assert exists(file_name)


@pytest.mark.parametrize('s,expected', [("1+1", 2), ("10-6", 4)])
def test_task15(s, expected):
    assert text_operation.task15(s) == expected


"""
Try to create some test with parametrization for your own tasks with big values, passing thinks with different types
Try to break your own solution with test improve code so this tests passed your own tests.
"""



"""
Create code for some opererational system (e.g. check if you have proper OS, if you have some directionary, is this the proper user)
"""


"""
Using this class for covid cases or function to get some stats about covid and check if works, how to cruch it (wrong name of country etc.)
MORE ADVANCED you can try to use Mock
"""