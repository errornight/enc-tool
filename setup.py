from setuptools import setup, find_packages
import os


directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='enc_tool',
    version='1.0',
    packages=find_packages(),
    description="A tool to encrypt and decrypt your data! \
                \n Use it to make  your messages and files safe...",
    long_description= long_description,
    long_description_content_type="text/markdown",
    author= "Night Error",
    author_email="night.error.go@gmail.com",

    entry_points={
        'console_scripts': [
            'enc = encrypter_decrypter.main:main',
        ],
    },
    install_requires=[
        'colorama', 'cryptography',
    ],
)
