import pytest
import os


@pytest.fixture
def existing_sql_dict():
    from sql_dict.sql_dict import SQLDict
    return SQLDict(os.path.abspath(os.path.dirname(__file__))+'db/test.db')


@pytest.fixture
def new_sql_dict():
    from sql_dict.sql_dict import SQLDict
    key = 'java'
    value = 'best language'
    return SQLDict(':memory:', [(key, value)])


def test_create_new(new_sql_dict):
    key = 'java'
    value = 'best language'
    got = new_sql_dict[key]
    assert got == value

def test_set_value(new_sql_dict):
    key = 'rust'
    value = 'favorite language'
    new_sql_dict[key] = value
    got = new_sql_dict[key]
    assert got == value