from setuptools import setup, find_packages
import os
from encrypter_decrypter.config import config

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name=config.NAME,
    version= config.VERSION,
    packages=find_packages(),
    description= config.DESCRIPTION,
    long_description= long_description,
    long_description_content_type="text/markdown",
    author= "Night Error",
    author_email= "night.error.go@gmail.com",

    entry_points={
        'console_scripts': [
            'enc = encrypter_decrypter.main:main',
        ],
    },
    install_requires=[
        'colorama', 'cryptography',
    ],
)
