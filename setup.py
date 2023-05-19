from setuptools import setup, find_packages
import os
import json

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# read data from config file
with open(os.path.join(directory, "encrypter_decrypter/config/config.json"), "r") as file:
    config = json.load(file)

setup(
    name=config['name'],
    version= config['version'],
    packages=find_packages(),
    description= config['description'],
    long_description= long_description,
    long_description_content_type="text/markdown",
    author= config['author'],
    author_email= config['author_email'],

    entry_points={
        'console_scripts': [
            'enc = encrypter_decrypter.main:main',
        ],
    },
    install_requires=[
        'colorama', 'cryptography',
    ],
)
