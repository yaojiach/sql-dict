from collections.abc import MutableMapping
from contextlib import suppress
from operator import itemgetter
import sqlite3


class SQLDict(MutableMapping):
    def __init__(self, dbname, items=[], **kwds):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)
        c = self.conn.cursor()
        with suppress(sqlite3.OperationalError):
            c.execute('create table dict (key text, value text)')
            c.execute('create unique index kndx on dict (key)')
        self.update(items, **kwds)

    def __setitem__(self, key, value):
        if key in self:
            del self[key]
        with self.conn as c:
            c.execute('insert into dict values (?, ?)', (key, value))
        
    def __getitem__(self, key):
        c = self.conn.execute('select value from dict where key = ?', (key,))
        row = c.fetchone()
        if row is None:
            raise KeyError(key)
        return row[0]

    def __delitem__(self, key):
        if key not in self:
            raise KeyError(key)
        with self.conn as c:
            c.execute('delete from dict where key = ?', (key,))

    def __len__(self):
        return next(self.conn.execute('select count(*) from dict'))[0]

    def __iter__(self):
        c = self.conn.execute('select key from dict')
        return map(itemgetter[0], c.fetchall())

    def __repr__(self):
        return f'{type(self.__name__)}(dbname={self.dbname!r}, items={list(self.items())})'

    def close(self):
        self.conn.close()
