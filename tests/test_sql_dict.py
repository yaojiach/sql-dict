import pytest
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@pytest.fixture
def existing_sql_dict(tmpdir):
    from sql_dict.sql_dict import SQLDict
    db = tmpdir.join('test.db')
    logger.debug(f'Set tmp db at: {db}')
    return SQLDict(db)


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


def test_create_new_on_disc(existing_sql_dict):
    key = 'javascript'
    value = 'vue is awesome'
    existing_sql_dict[key] = value
    got = existing_sql_dict[key]
    assert got == value


def test_overwrite_key(new_sql_dict):
    key = 'java'
    value = 'sure about that?'
    new_sql_dict[key] = value
    got = new_sql_dict[key]
    assert got == value


def test_delete_item(new_sql_dict):
    key = 'java'
    del new_sql_dict[key]
    with pytest.raises(KeyError):
        assert new_sql_dict[key]


def test_delete_non_existent_key(new_sql_dict):
    key = 'elixir'
    with pytest.raises(KeyError):
        assert new_sql_dict.__delitem__(key)


def test_len(new_sql_dict):
    assert len(new_sql_dict) == 1