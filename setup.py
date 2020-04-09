import io
import re

from collections import OrderedDict
from setuptools import setup, find_packages


with io.open('sql_dict/__init__.py', 'rt', encoding='utf8') as f:
    version = re.search(r'__version__ = \'(.*?)\'', f.read()).group(1)

setup(
    name='sql_dict',
    version=version,
    url='https://github.com/jucyai/sql_dict',
    project_urls=OrderedDict((
        ('Code', 'https://github.com/jucyai/sql_dict'),
        ('Issue tracker', 'https://github.com/jucyai/sql_dict/issues'),
    )),
    license='MIT',
    author='Jiachen Yao',
    maintainer='Jiachen Yao',
    description='Dictionary on disk with SQLite.',
    long_description='Dictionary on disk with SQLite.',
    packages=find_packages(exclude=['tests', 'db']),
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest',
            'tox'
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)